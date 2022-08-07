abstract class Fighter {

    boolean isVulnerable() {
        return false;
    }

    abstract int damagePoints(Fighter fighter);

    public String toString() {
        return "Fighter is a " + this.getClass().getName();
    }
    
}

class Warrior extends Fighter {

    @Override
    int damagePoints(Fighter wizard) {
        return wizard.isVulnerable() ? 10 : 6;
    }
}

class Wizard extends Fighter {
    boolean spellPrepared = false;

    @Override
    boolean isVulnerable() {
        return !spellPrepared;
    }

    @Override
    int damagePoints(Fighter warrior) {
        return spellPrepared ? 12 : 3;
    }

    void prepareSpell() {
        spellPrepared = true;
    }

}
