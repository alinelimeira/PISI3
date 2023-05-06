// ignore_for_file: prefer_const_constructors

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';

class PomodoroCreateField extends StatefulWidget {
  const PomodoroCreateField({super.key});

  @override
  State<PomodoroCreateField> createState() => _PomodoroCreateFieldState();
}

var uid = FirebaseAuth.instance.currentUser!.uid;

class _PomodoroCreateFieldState extends State<PomodoroCreateField> {
  @override
  Widget build(BuildContext context) {
    return FloatingActionButton(
      onPressed: () {
        showDialog(
            context: context,
            builder: (context) {
              var nomeControler = TextEditingController();
              var tempoFocoControler = TextEditingController();
              var tempoDescansoControler = TextEditingController();
              var cicloControler = TextEditingController();
              return AlertDialog(
                title: Text('Defina seu Pomodoro'),
                content: SingleChildScrollView(
                  child: Column(children: [
                    TextFormField(
                      autofocus: true,
                      decoration: InputDecoration(hintText: 'Nome'),
                      controller: nomeControler,
                    ),
                    TextFormField(
                      decoration: InputDecoration(hintText: 'Tempo de foco'),
                      controller: tempoFocoControler,
                    ),
                    TextFormField(
                      decoration:
                          InputDecoration(hintText: 'Tempo de descanso'),
                      controller: tempoDescansoControler,
                    ),
                    TextFormField(
                      decoration: InputDecoration(hintText: 'Ciclos'),
                      controller: cicloControler,
                    )
                  ]),
                ),
                actions: [
                  TextButton(
                      onPressed: () {
                        FirebaseFirestore.instance
                            .collection('users')
                            .doc(uid)
                            .collection('pomodoro')
                            .doc(nomeControler.text)
                            .set({
                          'nome': nomeControler.text,
                          'tempoDescanso':
                              int.parse(tempoDescansoControler.text),
                          'tempoFoco': int.parse(tempoFocoControler.text),
                          'ciclos': int.parse(cicloControler.text),
                          'ciclosEstudados': 0,
                          'tempoEstudoMinutos': 0,
                        });

                        Navigator.of(context).pop();
                      },
                      child: Text('Pronto'))
                ],
              );
            });
      },
      child: const Icon(
        Icons.add,
        color: Colors.blue,
      ),
    );
  }
}
