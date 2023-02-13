import 'package:flutter/material.dart';

class PrimaryOutlinedButton extends StatefulWidget {
  final String title;
  final Color color;
  final Color textColor;
  final Function() onPressed;
  final BorderRadius? borderRadius;
  const PrimaryOutlinedButton(
      {Key? key,
      required this.title,
      this.color = Colors.greenAccent,
      this.textColor = const Color(0xFF00b894),
      required this.onPressed,
      this.borderRadius})
      : super(key: key);

  @override
  State<PrimaryOutlinedButton> createState() => _PrimaryOutlinedButtonState();
}

class _PrimaryOutlinedButtonState extends State<PrimaryOutlinedButton> {
  late final BorderRadius borderRadius;

  @override
  void initState() {
    super.initState();
    borderRadius = widget.borderRadius ?? BorderRadius.circular(8);
  }

  @override
  Widget build(BuildContext context) {
    return OutlinedButton(
      onPressed: widget.onPressed,
      style: OutlinedButton.styleFrom(
          minimumSize: const Size.fromWidth(160),
          padding: const EdgeInsets.all(6),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
          side: BorderSide(color: widget.color, width: 2)),
      child: Text(
        widget.title,
        style: TextStyle(
            color: widget.textColor, fontSize: 16, fontWeight: FontWeight.bold),
      ),
    );
  }
}

//------------------------------------------------------------------------------

class BlockedButton extends StatefulWidget {
  final String title;
  final Color color;
  final Color textColor;
  final Function() onPressed;
  final BorderRadius? borderRadius;
  const BlockedButton(
      {Key? key,
      required this.title,
      this.color = const Color(0xFFE32929),
      this.textColor = const Color(0xFFE32929),
      required this.onPressed,
      this.borderRadius})
      : super(key: key);

  @override
  State<BlockedButton> createState() => _BlockedButtonState();
}

class _BlockedButtonState extends State<BlockedButton> {
  late final BorderRadius borderRadius;

  @override
  void initState() {
    super.initState();
    borderRadius = widget.borderRadius ?? BorderRadius.circular(8);
  }

  @override
  Widget build(BuildContext context) {
    return OutlinedButton(
      onPressed: widget.onPressed,
      style: OutlinedButton.styleFrom(
          minimumSize: const Size.fromWidth(160),
          padding: const EdgeInsets.all(6),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
          side: BorderSide(color: widget.color, width: 2)),
      child: Text(
        widget.title,
        style: TextStyle(
            color: widget.textColor, fontSize: 16, fontWeight: FontWeight.bold),
      ),
    );
  }
}

//------------------------------------------------------------------------------

class PrimaryButton extends StatefulWidget {
  final String title;
  final Color color;
  final Color textColor;
  final Function() onPressed;
  final BorderRadius? borderRadius;
  const PrimaryButton(
      {Key? key,
      required this.title,
      this.color = const Color(0xFF55EFC4),
      this.textColor = Colors.black,
      required this.onPressed,
      this.borderRadius})
      : super(key: key);

  @override
  State<PrimaryButton> createState() => _PrimaryButtonState();
}

class _PrimaryButtonState extends State<PrimaryButton> {
  late final BorderRadius borderRadius;

  @override
  void initState() {
    super.initState();
    borderRadius = widget.borderRadius ?? BorderRadius.circular(8);
  }

  @override
  Widget build(BuildContext context) {
    return TextButton(
      onPressed: widget.onPressed,
      style: TextButton.styleFrom(
          minimumSize: const Size.fromWidth(160),
          padding: const EdgeInsets.all(6),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
          backgroundColor: widget.color),
      child: Text(
        widget.title,
        style: TextStyle(
            color: widget.textColor, fontSize: 16, fontWeight: FontWeight.bold),
      ),
    );
  }
}

//------------------------------------------------------------------------------

class SecondaryButton extends StatefulWidget {
  final String title;
  final Color color;
  final Color textColor;
  final Function() onPressed;
  final BorderRadius? borderRadius;
  const SecondaryButton(
      {Key? key,
      required this.title,
      this.color = const Color(0xFF00ACEE),
      this.textColor = Colors.white,
      required this.onPressed,
      this.borderRadius})
      : super(key: key);

  @override
  State<SecondaryButton> createState() => _SecondaryButtonState();
}

class _SecondaryButtonState extends State<SecondaryButton> {
  late final BorderRadius borderRadius;

  @override
  void initState() {
    super.initState();
    borderRadius = widget.borderRadius ?? BorderRadius.circular(8);
  }

  @override
  Widget build(BuildContext context) {
    return TextButton(
      onPressed: widget.onPressed,
      style: TextButton.styleFrom(
          minimumSize: const Size.fromWidth(160),
          padding: const EdgeInsets.all(6),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
          backgroundColor: widget.color),
      child: Text(
        widget.title,
        style: TextStyle(
            color: widget.textColor, fontSize: 16, fontWeight: FontWeight.bold),
      ),
    );
  }
}
