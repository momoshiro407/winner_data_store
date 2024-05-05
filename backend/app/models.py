from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    # ユーザID
    id = db.Column(db.Integer, primary_key=True)
    # ユーザ名
    name = db.Column(db.String(200), nullable=False)
    # メールアドレス
    email = db.Column(db.String(200), nullable=False)
    # パスワードのハッシュ
    password_hash = db.Column(db.String(200), nullable=False)
    # ロール（管理者: 1, 一般ユーザ: 2）
    role = db.Column(db.Integer, nullable=False)


class Team(db.Model):
    __tablename__ = 'teams'
    # チームID
    id = db.Column(db.Integer, primary_key=True)
    # 所属リーグ区分（J1: 1, J2: 2, J3: 3）
    devision = db.Column(db.Integer, nullable=False)
    # チーム名
    name = db.Column(db.String(200), nullable=False)
    # チーム名の略称
    short_name = db.Column(db.String(200), nullable=False)

    # リレーションの定義
    match_result = db.relationship('MatchResult')


class Season(db.Model):
    __tablename__ = 'seasons'
    # シーズンID
    id = db.Column(db.Integer, primary_key=True)
    # シーズンの表示名
    display_name = db.Column(db.String(200), nullable=False)
    # シーズンの開始日
    start_date = db.Column(db.Date, nullable=False)
    # シーズンの終了日
    end_date = db.Column(db.Date, nullable=False)

    # リレーションの定義
    match_result = db.relationship('MatchResult')


class MatchResult(db.Model):
    __tablename__ = 'match_results'
    # 試合結果ID
    id = db.Column(db.Integer, primary_key=True)
    # 試合日
    match_date = db.Column(db.Date, nullable=False)
    # シーズンID
    season_id = db.Column(
        db.Integer, db.ForeignKey('seasons.id'), nullable=False)
    # 節
    section = db.Column(db.Integer)
    # 大会カテゴリID
    convention_category_id = db.Column(db.Integer, db.ForeignKey(
        'convention_categories.id'), nullable=False)
    # ホームチームID
    home_team_id = db.Column(
        db.Integer, db.ForeignKey('teams.id'), nullable=False)
    # アウェイチームID
    away_team_id = db.Column(
        db.Integer, db.ForeignKey('teams.id'), nullable=False)
    # ホームチーム得点
    home_team_score = db.Column(db.Integer, nullable=False)
    # アウェイチーム得点
    away_team_score = db.Column(db.Integer, nullable=False)
    # 当選金額
    winning_amounnt = db.Column(db.Integer, nullable=False)
    # 当選口数
    total_winners = db.Column(db.Integer, nullable=False)

    # リレーションの定義
    season = db.relationship('Season')
    team = db.relationship('Team')
    team = db.relationship('ConventionCategory')


class ConventionCategory(db.Model):
    __tablename__ = 'convention_categories'
    # 大会カテゴリID
    id = db.Column(db.Integer, primary_key=True)
    # 大会カテゴリ名
    name = db.Column(db.String(200), nullable=False)
    # WINNERサイト上の表示名
    display_name = db.Column(db.String(200), nullable=False)

    # リレーションの定義
    match_result = db.relationship('MatchResult')
