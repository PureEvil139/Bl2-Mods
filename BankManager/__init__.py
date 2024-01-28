import unrealsdk

from Mods.ModMenu import EnabledSaveType, Hook, ModTypes, Options, RegisterMod, SDKMod


class BankManager(SDKMod):
    Name: str = "BankManager"
    Author = "PureEvil139"
    Description: str = "Customize the size of your bank!"
    Version: str = "1.0"

    Types: ModTypes = ModTypes.Gameplay
    SaveEnabledState: EnabledSaveType = EnabledSaveType.LoadWithSettings

    bankSize: Options.Slider = Options.Slider(
        "bank", "Change the size of your character's bank<br>Default is 6", 6, 0, 200, 1
    )
    Options = [bankSize]

    @Hook("WillowGame.WillowHUD.CreateWeaponScopeMovie")
    def _GameLoad(self, caller: unrealsdk.UObject, function: unrealsdk.UFunction, params: unrealsdk.FStruct) -> bool:
        PC = unrealsdk.GetEngine().GamePlayers[0].Actor
        if PC and PC.Pawn:
            PC.Pawn.InvManager.TheBank.ChestSlots = self.bankSize.CurrentValue
        return True

    def ModOptionChanged(self, option, newValue) -> None:
        if option == self.bankSize:
            PC = unrealsdk.GetEngine().GamePlayers[0].Actor
            if PC and PC.Pawn:
                PC.Pawn.InvManager.TheBank.ChestSlots = newValue


RegisterMod(BankManager())