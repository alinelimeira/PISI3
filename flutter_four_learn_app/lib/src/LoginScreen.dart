// ignore_for_file: file_names

import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:flutter_four_learn_app/util/textButtons.dart';
import 'package:flutter_four_learn_app/util/textFormFields.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({Key? key}) : super(key: key);

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  late final TextEditingController _name;
  late final TextEditingController _email;
  late final TextEditingController _password;
  late final TextEditingController _telefone;

  @override
  void initState() {
    _name = TextEditingController();
    _email = TextEditingController();
    _password = TextEditingController();
    _telefone = TextEditingController();
    super.initState();
  }

  @override
  void dispose() {
    _name.dispose();
    _email.dispose();
    _password.dispose();
    _telefone.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    //O contexto é a tela
    final size = MediaQuery.of(context).size;

    return Scaffold(
      backgroundColor: Colors.white,

      // Oraginzar o body em colunas
      body: SingleChildScrollView(
        child: SizedBox(
          height: size.height,
          width: size.width,
          child: Column(
            children: [
              Expanded(
                  child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Image.asset('assets/images/4learnLogo.png'),
                ],
              )),
              Container(
                padding: const EdgeInsets.symmetric(
                  horizontal: 30,
                  vertical: 30,
                ),
                decoration: const BoxDecoration(color: Colors.white),
                child: Column(
                  children: [
                    //email
                    Padding(
                      padding: const EdgeInsets.only(bottom: 15),
                      child: OutlinedTextFormField(
                        controller: _email,
                        enableSuggestions: false,
                        autocorrect: false,
                        keyboardType: TextInputType.emailAddress,
                        hintText: 'Email',
                        isDense: true,
                        icon: Icon(Icons.email_outlined),
                      ),
                    ),

                    // Senha
                    Padding(
                      padding: const EdgeInsets.only(bottom: 80),
                      child: OutlinedTextFormField(
                        controller: _password,
                        obscureText: true,
                        enableSuggestions: false,
                        autocorrect: false,
                        hintText: 'Senha',
                        isDense: true,
                        icon: Icon(Icons.lock_outline),
                      ),
                    ),

                    // BOTÂO PARA ENTRAR
                    SizedBox(
                      height: 45,
                      child: PrimaryOutlinedButton(
                        title: 'ENTRAR',
                        onPressed: () async {
                          final email = _email.text;
                          final password = _password.text;
                          try {
                            final UserCredential = await FirebaseAuth.instance
                                .signInWithEmailAndPassword(
                                    email: email, password: password);
                            Navigator.of(context).pushNamed('/MainScreen');
                            //print(UserCredential);
                          } on FirebaseAuthException catch (e) {
                            if (e.code == 'user-not-found') {
                              print('user not found');
                            } else if (e.code == 'wrong-password') {
                              print('wrong password');
                            }
                          }
                        },
                      ),
                    ),

                    //Esqueceu senha?
                    Align(
                      alignment: Alignment.centerLeft,
                      //Padding: Espaçamento entre o texto 'esqueci sinha' e os botões.
                      child: Padding(
                        padding: const EdgeInsets.only(top: 5),
                        child: TextButton(
                          onPressed: () {},
                          child: const Text(
                            'Esqueceu a senha?',
                            style: TextStyle(
                              color: Colors.green,
                            ),
                          ),
                        ),
                      ),
                    ),

                    // DIVISOR COM 'ou'
                    Padding(
                      padding: const EdgeInsets.only(bottom: 10),
                      child: Row(
                        children: const [
                          Expanded(
                            child: Divider(
                              color: Colors.green,
                              thickness: 2,
                            ),
                          ),
                          Padding(
                            padding: EdgeInsets.symmetric(horizontal: 15),
                            child: Text('ou'),
                          ),
                          Expanded(
                            child: Divider(
                              color: Colors.green,
                              thickness: 2,
                            ),
                          ),
                        ],
                      ),
                    ),

                    //Botão: CRIAR CONTA
                    SizedBox(
                      height: 45,
                      child: PrimaryOutlinedButton(
                          title: 'CRIAR CONTA',
                          onPressed: () {
                            Navigator.of(context).pushNamed('/Register');
                          }),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
