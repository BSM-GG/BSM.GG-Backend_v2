from app.controller.summoner.types.match_type import ParticipantType, MatchType, MatchResponseType
from app.controller.summoner.types.summoner_type import SummonerType
from app.controller.summoner.types.this_week_type import ThisWeekType
from app.repository.riot.riot_repository import RiotRepository
from app.repository.summoner.summoner_repository import SummonerRepository
from app.repository.user.user_repository import UserRepository
from app.service.riot.riot_get_service import RiotGetService
from app.service.user.user_get_service import UserGetService
from app.utility.error.errors import SummonerNotFound


def to_summoner_type(summoner, user):
    summoner_model = SummonerType(
        game_name="",
        tag_line="",
        profile_icon=0,
        level=0,
        solo_tier="",
        solo_lp=0,
        solo_wins=0,
        solo_loses=0,
        flex_tier="",
        flex_lp=0,
        flex_wins=0,
        flex_loses=0,
        most_champions=[],
        email="",
        code=0,
        nickname="",
        name="",
        role="",
        is_graduate=False,
        enrolled_at=0,
        grade=0,
        class_no=0,
        student_no=0,
        rank_point=0,
        ranking=0,
    )
    if summoner is not None:
        summoner_model.game_name = summoner.game_name
        summoner_model.tag_line = summoner.tag_line
        summoner_model.profile_icon = summoner.profile_icon
        summoner_model.level = summoner.level
        summoner_model.solo_tier = summoner.solo_tier
        summoner_model.solo_lp = summoner.solo_lp
        summoner_model.solo_wins = summoner.solo_wins
        summoner_model.solo_loses = summoner.solo_loses
        summoner_model.flex_tier = summoner.flex_tier
        summoner_model.flex_lp = summoner.flex_lp
        summoner_model.flex_wins = summoner.flex_wins
        summoner_model.flex_loses = summoner.flex_loses
        summoner_model.most_champions = [summoner.most1, summoner.most2, summoner.most3]
        summoner_model.rank_point = summoner.rank_point
        summoner_model.ranking = summoner.ranking
    if user is not None:
        summoner_model.email = user.email
        summoner_model.code = user.code
        summoner_model.nickname = user.nickname
        summoner_model.name = user.name
        summoner_model.role = user.role
        summoner_model.is_graduate = user.is_graduate
        summoner_model.enrolled_at = user.enrolled_at
        summoner_model.grade = user.grade
        summoner_model.class_no = user.class_no
        summoner_model.student_no = user.student_no
    return summoner_model


class SummonerService:

    def __init__(self):
        self.user_get_service = UserGetService()
        self.riot_get_service = RiotGetService()
        self.summoner_repository = SummonerRepository()
        self.riot_repository = RiotRepository()

    async def find_summoners(self):
        users = await self.riot_repository.get_users()
        user_puuids = list(map(lambda u: u.puuid, users))
        summoners = await self.summoner_repository.find_summoners_rank_by_puuids(user_puuids)
        response = []
        for i in range(len(summoners)):
            response.append(to_summoner_type(summoners[i], users[i]))
        return response

    async def find_summoner(self, game_name: str, tag_line: str):
        summoner = await self.summoner_repository.find_summoner_rank(game_name, tag_line)
        if summoner is None:
            raise SummonerNotFound(game_name=game_name, tag_line=tag_line)
        user = await self.user_get_service.get_user_by_puuid(summoner.puuid)
        return to_summoner_type(summoner, user)

    async def find_lol_chang(self):
        lol_chang = await self.summoner_repository.find_lol_chang()
        user = await self.user_get_service.get_user_by_puuid(lol_chang.puuid)
        return ThisWeekType(
            game_name=lol_chang.game_name,
            tag_line=lol_chang.tag_line,
            profile_icon=lol_chang.profile_icon,
            level=lol_chang.level,
            solo_tier=lol_chang.solo_tier,
            solo_lp=lol_chang.solo_lp,
            solo_wins=lol_chang.solo_wins,
            solo_loses=lol_chang.solo_loses,
            flex_tier=lol_chang.flex_tier,
            flex_lp=lol_chang.flex_lp,
            flex_wins=lol_chang.flex_wins,
            flex_loses=lol_chang.flex_loses,
            most_champions=[lol_chang.most1, lol_chang.most2, lol_chang.most3],
            played_games=lol_chang.played_games,
            win_games=lol_chang.win_games,
            lose_games=lol_chang.lose_games,
            kill=lol_chang.kill,
            death=lol_chang.death,
            assist=lol_chang.assist,
            gold_spent=lol_chang.gold_spent,
            skill_use=lol_chang.skill_use,
            play_time=lol_chang.play_time,
            spell_use=lol_chang.spell_use,
            damage=lol_chang.damage,
            gain_damage=lol_chang.gain_damage,
            ward_place=lol_chang.ward_place,
            vision_score=lol_chang.vision_score,
            cs=lol_chang.cs,
            email=user.email,
            code=user.code,
            nickname=user.nickname,
            name=user.name,
            role=user.role,
            is_graduate=user.is_graduate,
            enrolled_at=user.enrolled_at,
            grade=user.grade,
            class_no=user.class_no,
            student_no=user.student_no,
            ranking=lol_chang.ranking,
        )

    async def get_matches(self, name: str, page: int = 0):
        game_name, tag_line = name.split("+")
        offset = page * 10
        limit = 10

        summoner = await self.riot_get_service.get_summoner_by_game_name_and_tag_line(game_name, tag_line)
        matches = await self.riot_get_service.get_matches_by_puuid(summoner.puuid, offset, limit)
        match_models = []
        for match in matches:
            win = False
            participant_models = []
            participants = await self.riot_get_service.get_participant_in_match(match.match_id)
            for participant in participants:
                participant_models.append(ParticipantType(
                    game_name=participant.game_name,
                    tag_line=participant.tag_line,
                    solo_tier=participant.solo_tier,
                    level=participant.level,
                    champion=participant.champion,
                    champion_level=participant.champion_level,
                    spell1=participant.spell1,
                    spell2=participant.spell2,
                    main_perk=participant.main_perk,
                    sub_perk=participant.sub_style,
                    kill=participant.kill,
                    death=participant.death,
                    assist=participant.assist,
                    damage=participant.damage,
                    gain_damage=participant.gain_damage,
                    sight_ward=participant.sight_ward,
                    vision_ward=participant.vision_ward,
                    vision_score=participant.vision_score,
                    items=[
                        participant.item1,
                        participant.item2,
                        participant.item3,
                        participant.item4,
                        participant.item5,
                        participant.item6
                    ],
                    ward=participant.ward,
                    is_summoner=False
                ))
                if participant.puuid == summoner.puuid:
                    participant_models[-1].is_summoner = True
                    win = participant.win

            match_models.append(MatchType(
                game_type=match.game_type,
                win=win,
                game_start_at=match.game_start_at,
                game_duration=match.game_duration,
                participants=participant_models,
            ))
        return MatchResponseType(matches=match_models, page=page)


