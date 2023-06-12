---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/aura.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: xstaxy-1 | **Latest Version Tag**: aura_v0.4.5 | **Custom Port**: 117

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf aura
git clone https://github.com/aura-nw/aura.git
cd aura
git checkout aura_v0.4.5

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.aura/cosmovisor/upgrades/v0.4.5/bin
mv build/aurad $HOME/.aura/cosmovisor/upgrades/v0.4.5/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
