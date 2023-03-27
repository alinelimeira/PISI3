// ignore_for_file: prefer_const_constructors

import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter_four_learn_app/util/textButtons.dart';
import 'package:flutter_four_learn_app/util/textFields.dart';

class ProfileScreen extends StatefulWidget {
  const ProfileScreen({Key? key}) : super(key: key);

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

final FirebaseFirestore _firestore = FirebaseFirestore.instance;
final CollectionReference _Collection = _firestore.collection('user');

class FirebaseCrud {
  static Stream<QuerySnapshot> readData() {
    CollectionReference notesCollection = _Collection;
    return notesCollection.snapshots();
  }
}

class _ProfileScreenState extends State<ProfileScreen> {
  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;

    String usuario = '';

    String? email = FirebaseAuth.instance.currentUser?.email;

    var uid = FirebaseAuth.instance.currentUser!.uid;

    CollectionReference collectionReference =
        FirebaseFirestore.instance.collection('users');

    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 48,
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [Text('Perfil')],
        ),
        automaticallyImplyLeading: false,
        backgroundColor: Colors.blue,
      ),
      backgroundColor: Colors.white,
      body: SizedBox(
        height: size.height,
        width: size.width,
        child: Column(
          children: [
            Padding(
              padding: const EdgeInsets.only(top: 24.0),
              child: Container(
                width: 292,
                height: 88,
                decoration: BoxDecoration(
                    color: Color(0xFF44CDEB),
                    borderRadius: BorderRadius.circular(10)),
                child: Row(
                  children: [
                    Icon(
                      Icons.person,
                      size: 40,
                    ),
                    FutureBuilder<DocumentSnapshot>(
                      future: collectionReference.doc(uid).get(),
                      builder: (BuildContext context,
                          AsyncSnapshot<DocumentSnapshot> snapshot) {
                        if (snapshot.hasError) {
                          return Text('ERRO');
                        }
                        if (snapshot.hasData && !snapshot.data!.exists) {
                          return Text('Not exist');
                        }
                        if (snapshot.connectionState == ConnectionState.done) {
                          Map<String, dynamic> data =
                              snapshot.data!.data() as Map<String, dynamic>;
                          usuario = data['uid'];
                          return Text(
                            "${data['uid']}",
                            textAlign: TextAlign.center,
                            style: TextStyle(fontSize: 16),
                          );
                        }
                        return Text('loading');
                      },
                    ),
                  ],
                ),
              ),
            ),
            Divider(
              color: Colors.black,
              thickness: 1,
            ),
            SizedBox(
                height: 45,
                child: BlockedButton(
                    title: 'SAIR',
                    onPressed: () async {
                      FirebaseAuth.instance.signOut();
                      Navigator.of(context).pushNamed('/');
                    }))
          ],
        ),
      ),
    );
  }
}
