// ignore_for_file: prefer_const_constructors

import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter_four_learn_app/util/textButtons.dart';
import 'package:flutter_four_learn_app/util/textFields.dart';

class MainMenuScreen extends StatefulWidget {
  const MainMenuScreen({Key? key}) : super(key: key);

  @override
  State<MainMenuScreen> createState() => _MainMenuScreenState();
}

class _MainMenuScreenState extends State<MainMenuScreen> {
  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;

    return Scaffold(
      appBar: AppBar(
        toolbarHeight: 48,
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image.asset(
              'assets/images/4learnLogo.png',
              fit: BoxFit.contain,
              height: 52,
            ),
          ],
        ),
        automaticallyImplyLeading: false,
        backgroundColor: Colors.blue,
      ),
      backgroundColor: Colors.white,
      body: SizedBox(
        height: size.height,
        width: size.width,
        child: Column(children: [
          Padding(
            padding: EdgeInsets.fromLTRB(8, 48, 8, 8),
            child: StandardTextField(
              title:
                  'Olá, eu sou o 4Learn e tenho como objetivo lhe auxiliar nos estudos durante sua jornada no Ensino Médio!',
            ),
          ),
          Padding(
            padding: EdgeInsets.all(8.0),
            child: StandardTextField(
                title:
                    'Tenho uma ferramenta de aprendizado em máquina, que respondendo algumas perguntas você saberá se vai passar de ano ou não.'),
          ),
          Padding(
            padding: EdgeInsets.all(8.0),
            child: StandardTextField(
                title:
                    'Para ter acesso ao formulário, basta clicar no botão a baixo. Vamos lá?!'),
          ),
          Padding(
            padding: const EdgeInsets.only(top: 24),
            child: SizedBox(
              height: 45,
              child: PrimaryOutlinedButton(
                title: 'Forumulário',
                onPressed: () {
                  Navigator.of(context).pushNamed('/ProfileScreen');
                },
              ),
            ),
          ),
        ]),
      ),
    );
  }
}
