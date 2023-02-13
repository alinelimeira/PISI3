// ignore_for_file: file_names

import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:flutter_four_learn_app/firebase_options.dart';
import 'package:flutter_four_learn_app/src/LoginScreen.dart';

class FirebaseAuth extends StatelessWidget {
  const FirebaseAuth({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // ignore: prefer_const_constructors
    return Scaffold(
        backgroundColor: Colors.blueGrey,
        body: FutureBuilder(
          future: Firebase.initializeApp(
            options: DefaultFirebaseOptions.currentPlatform,
          ),
          builder: (context, snapshot) {
            switch (snapshot.connectionState) {
              case ConnectionState.done:
                return LoginScreen();
              default:
                return const Text('Loading...');
            }
          },
        ));
  }
}
