// ignore_for_file: prefer_const_constructors, prefer_const_literals_to_create_immutables, sort_child_properties_last

import 'package:flutter/material.dart';
import 'package:flutter_four_learn_app/src/MainMenuScreen.dart';
import 'package:flutter_four_learn_app/src/ProfileScreen.dart';
import 'package:flutter_four_learn_app/src/PomodoroListScreen.dart';
import 'package:flutter_four_learn_app/src/StudyTime.dart';

import 'CodexScreen.dart';

class MainScreen extends StatefulWidget {
  const MainScreen({Key? key}) : super(key: key);

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  int screenAtual = 0;
  late PageController pc;

  @override
  void initState() {
    super.initState();
    pc = PageController(initialPage: screenAtual);
  }

  setScreenAtual(screen) {
    setState(() {
      screenAtual = screen;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: PageView(
        controller: pc,
        children: [
          MainMenuScreen(),
          ProfileScreen(),
          PomodoroListScreen(),
          CodexScreen(CodexScreen.createSampleData()),
          StudyTime()
        ],
        onPageChanged: setScreenAtual,
      ),
      bottomNavigationBar: Container(
        decoration:
            BoxDecoration(border: Border(top: BorderSide(color: Colors.black))),
        child: BottomNavigationBar(
          currentIndex: screenAtual,
          items: [
            BottomNavigationBarItem(icon: Icon(Icons.house), label: 'Menu'),
            BottomNavigationBarItem(icon: Icon(Icons.person), label: 'Perfil'),
            BottomNavigationBarItem(icon: Icon(Icons.timer), label: 'Pomodoro'),
            BottomNavigationBarItem(
                icon: Icon(Icons.book), label: 'FocusCodex'),
            BottomNavigationBarItem(
                icon: Icon(Icons.menu_book), label: 'Study Time')
          ],
          onTap: (screen) {
            pc.animateToPage(screen,
                duration: Duration(milliseconds: 400), curve: Curves.ease);
          },
          backgroundColor: Colors.white,
          selectedItemColor: Colors.blue,
          unselectedItemColor: Colors.black,
          showSelectedLabels: false,
          showUnselectedLabels: false,
        ),
      ),
    );
  }
}
