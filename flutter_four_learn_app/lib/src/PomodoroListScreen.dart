import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';
import 'package:flutter_four_learn_app/src/Pomodoro.dart';
import 'package:flutter_four_learn_app/util/PomodoroCard.dart';

class PomodoroListScreen extends StatefulWidget {
  const PomodoroListScreen({super.key});

  @override
  State<PomodoroListScreen> createState() => _PomodoroListScreenState();
}

var uid = FirebaseAuth.instance.currentUser!.uid;
Stream collectionStream =
    FirebaseFirestore.instance.collection('users').snapshots();
Stream documentStream = FirebaseFirestore.instance
    .collection('users')
    .doc(uid)
    .collection('pomodoro')
    .snapshots();

class _PomodoroListScreenState extends State<PomodoroListScreen> {
  final Stream<QuerySnapshot> _userStream =
      FirebaseFirestore.instance.collection('users').snapshots();

  List<Object> _listPomodoro = [];

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    getUserPomodoroList();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 48,
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: const [Text('Pomodoro')],
        ),
        automaticallyImplyLeading: false,
        backgroundColor: Colors.blue,
      ),
      backgroundColor: Colors.white,
      body: SafeArea(
          child: ListView.builder(
        itemCount: _listPomodoro.length,
        itemBuilder: (context, index) {
          return PomodoroCard(_listPomodoro[index] as Pomodoro);
        },
      )),
    );
  }

  Future getUserPomodoroList() async {
    var data = await FirebaseFirestore.instance
        .collection('users')
        .doc(uid)
        .collection('pomodoro')
        .get();

    setState(() {
      _listPomodoro =
          List.from(data.docs.map((doc) => Pomodoro.fromSnapshot(doc)));
    });
  }
}
