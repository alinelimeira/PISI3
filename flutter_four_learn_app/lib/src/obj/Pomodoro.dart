class Pomodoro {
  String? nome;
  int? tempoFoco;
  int? tempoDescanso;
  int? ciclos;

  Pomodoro();

  Map<String, dynamic> toJson() => {
        'nome': nome,
        'tempoFoco': tempoFoco,
        'tempoDescanso': tempoDescanso,
        'ciclos': ciclos
      };

  Pomodoro.fromSnapshot(snapshot)
      : nome = snapshot.data()['nome'],
        tempoFoco = snapshot.data()['tempoFoco'],
        tempoDescanso = snapshot.data()['tempoDescanso'],
        ciclos = snapshot.data()['ciclos'];
}
