import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';

import '../util/PomodoroCard.dart';
import '../util/pomodoroCreateField.dart';
import 'obj/Pomodoro.dart';

class StudyTime extends StatefulWidget {
  const StudyTime({super.key});

  @override
  State<StudyTime> createState() => _StudyTimeState();
}

var uid = FirebaseAuth.instance.currentUser!.uid;

class _StudyTimeState extends State<StudyTime> {
  List<Object> _listPomodoro = [];

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    getUserPomodoroList();
  }

  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 48,
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: const [Text('Tempo estudado')],
        ),
        automaticallyImplyLeading: false,
        backgroundColor: Colors.blue,
      ),
      backgroundColor: Colors.white,
      body: SafeArea(
          child: ListView.builder(
        itemCount: _listPomodoro.length,
        itemBuilder: (context, index) {
          return PomodoroCardCicleTime(_listPomodoro[index] as Pomodoro);
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
