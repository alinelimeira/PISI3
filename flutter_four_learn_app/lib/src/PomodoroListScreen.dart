// ignore_for_file: prefer_const_constructors

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';
import 'package:flutter_four_learn_app/src/obj/Pomodoro.dart';
import 'package:flutter_four_learn_app/util/PomodoroCard.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:flutter_four_learn_app/util/pomodoroCreateField.dart';

class PomodoroListScreen extends StatefulWidget {
  const PomodoroListScreen({super.key});

  @override
  State<PomodoroListScreen> createState() => _PomodoroListScreenState();
}

var uid = FirebaseAuth.instance.currentUser!.uid;

class _PomodoroListScreenState extends State<PomodoroListScreen> {
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
      floatingActionButton: PomodoroCreateField(),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
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
