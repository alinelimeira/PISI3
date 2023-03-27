import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';
import 'package:intl/intl.dart';

import '../util/textButtons.dart';

class PomodoroScreen extends StatefulWidget {
  final String? name;
  final int? tempoFoco;
  final int? tempoDescanso;
  final int? ciclo;

  const PomodoroScreen(
      {required this.name,
      required this.tempoFoco,
      required this.tempoDescanso,
      required this.ciclo,
      super.key});

  @override
  State<PomodoroScreen> createState() => _PomodoroScreenState();
}

class _PomodoroScreenState extends State<PomodoroScreen> {
  var f = NumberFormat('00');
  int _cicloAtual = 0;
  int _seconds = 0;
  Timer _timer = Timer(Duration(milliseconds: 1), () {});
  late int? _minutes = widget.tempoFoco;
  bool descanso = true;
  Color backgroundColor = Color(0xFF55EFC4);
  @override
  Widget build(BuildContext context) {
    void _StopTimer() {
      _timer.cancel();
      _seconds = 0;
      _minutes = widget.tempoFoco;
    }

    void _StartTime() {
      if (_timer != null) {
        _StopTimer();
      }
      if (_minutes! > 0) {
        backgroundColor = Color(0xFFE32929);

        _seconds = _minutes! * 60;
      }
      if (_seconds >= 60) {
        _minutes = (_seconds / 60).floor();
        _seconds -= (_minutes! * 60);
      }
      _timer = Timer.periodic(const Duration(seconds: 1), (timer) {
        setState(() {
          if (_seconds > 0) {
            _seconds--;
          } else {
            if (_minutes! > 0) {
              _seconds = 59;
              _minutes = _minutes! - 1;
            } else {
              if (descanso == false) {
                _minutes = widget.tempoDescanso;
                backgroundColor = const Color(0xFF55EFC4);
                _cicloAtual++;
                descanso = true;
              } else {
                descanso = false;
                _minutes = widget.tempoFoco;
                backgroundColor = const Color(0xFFE32929);
                //_timer.cancel();
                print('Timer out');
              }
            }
          }
        });
      });
    }

    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 48,
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [Text('${widget.name}')],
        ),
        automaticallyImplyLeading: false,
        backgroundColor: Colors.blue,
      ),
      backgroundColor: backgroundColor,
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                "${_cicloAtual}/${widget.ciclo}",
                style: TextStyle(fontSize: 36),
              )
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                "${f.format(_minutes)} : ${f.format(_seconds)}",
                style: TextStyle(fontSize: 48),
              )
            ],
          ),
          SizedBox(
            height: 300,
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              SizedBox(
                height: 45,
                child: SecondaryButton(
                  onPressed: () {
                    setState(() {});
                    descanso = true;
                    backgroundColor = Color(0xFF55EFC4);
                    _StopTimer();
                  },
                  title: 'stop',
                ),
              ),
              SizedBox(
                height: 45,
                child: SecondaryButton(
                  onPressed: () {
                    descanso = false;
                    _StartTime();
                    //backgroundColor = Color(0xFFE32929);
                  },
                  title: 'Start',
                ),
              )
            ],
          )
        ],
      ),
    );
  }
}
