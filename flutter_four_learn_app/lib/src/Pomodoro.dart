class Pomodoro {
  String? nome;
  int? tempoFoco;
  int? tempoDescanso;

  Pomodoro();

  Map<String, dynamic> toJson() =>
      {'nome': nome, 'tempoFoco': tempoFoco, 'tempoDescanso': tempoDescanso};

  Pomodoro.fromSnapshot(snapshot)
      : nome = snapshot.data()['nome'],
        tempoFoco = snapshot.data()['tempoFoco'],
        tempoDescanso = snapshot.data()['tempoDescanso'];
}
