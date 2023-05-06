import 'package:flutter/material.dart';
import 'package:flutter_four_learn_app/src/obj/Pomodoro.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter_four_learn_app/src/PomodoroScreen.dart';

class PomodoroCard extends StatefulWidget {
  final Pomodoro _pomodoro;

  PomodoroCard(this._pomodoro);

  @override
  State<PomodoroCard> createState() => _PomodoroCardState();
}

class _PomodoroCardState extends State<PomodoroCard> {
  var uid = FirebaseAuth.instance.currentUser!.uid;

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Card(
        clipBehavior: Clip.hardEdge,
        color: Color(0xFF00ACEE),
        child: InkWell(
          splashColor: Colors.blue,
          onTap: () {
            Navigator.push(
                context,
                MaterialPageRoute(
                    builder: (context) => PomodoroScreen(
                          name: '${widget._pomodoro.nome}',
                          tempoFoco: widget._pomodoro.tempoFoco,
                          tempoDescanso: widget._pomodoro.tempoDescanso,
                          ciclo: widget._pomodoro.ciclos,
                          cicloEstudado: widget._pomodoro.ciclosEstudados,
                          tempoEstudoMinutos:
                              widget._pomodoro.tempoEstudoMinutos,
                        )));
          },
          child: Padding(
            padding: const EdgeInsets.all(12),
            child: Column(
              children: [
                Row(
                  children: [
                    Padding(
                      padding: const EdgeInsets.only(bottom: 10.0),
                      child: Text(
                        'Nome: ${widget._pomodoro.nome}',
                        style: TextStyle(fontSize: 16),
                      ),
                    ),
                    Spacer(),
                    IconButton(
                        onPressed: () {
                          print('tap tap');
                          final collection = FirebaseFirestore.instance
                              .collection('users')
                              .doc(uid)
                              .collection('pomodoro')
                              .doc('${widget._pomodoro.nome}')
                              .delete()
                              .then((doc) => print('pomodoro deleted'));

                          setState(() {});
                        },
                        icon: const Icon(Icons.delete))
                  ],
                ),
                Row(
                  children: [
                    Text(
                      'Tempo de Foco: ${widget._pomodoro.tempoFoco}, Tempo de descanso: ${widget._pomodoro.tempoDescanso}',
                      style: TextStyle(fontSize: 16),
                    ),
                  ],
                )
              ],
            ),
          ),
        ),
      ),
    );
  }
}

//---------------------------------------------------------------------------------------------------------------------------------------

class PomodoroCardCicleTime extends StatefulWidget {
  final Pomodoro _pomodoro;

  PomodoroCardCicleTime(this._pomodoro);

  @override
  State<PomodoroCardCicleTime> createState() => _PomodoroCardCicleTimeState();
}

class _PomodoroCardCicleTimeState extends State<PomodoroCardCicleTime> {
  var uid = FirebaseAuth.instance.currentUser!.uid;

  @override
  Widget build(BuildContext context) {
    return Container(
      child: Card(
        clipBehavior: Clip.hardEdge,
        color: Color(0xFF00ACEE),
        child: InkWell(
          splashColor: Colors.blue,
          child: Padding(
            padding: const EdgeInsets.all(12),
            child: Column(
              children: [
                Row(
                  children: [
                    Padding(
                      padding: const EdgeInsets.only(bottom: 10.0),
                      child: Row(children: [
                        Text(
                          'Nome: ${widget._pomodoro.nome}, Ciclos estudados: ${widget._pomodoro.ciclosEstudados}',
                          style: TextStyle(
                            fontSize: 16,
                          ),
                        ),
                      ]),
                    ),
                  ],
                ),
                Row(
                  children: [
                    Text(
                      'Tempo total estudado: ${widget._pomodoro.tempoEstudoMinutos} minutos',
                      style: TextStyle(fontSize: 16),
                    ),
                  ],
                )
              ],
            ),
          ),
        ),
      ),
    );
  }
}
