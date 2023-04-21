---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.2.2-store-fix | **Custom Port**: 43

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf nolus-core
git clone https://github.com/Nolus-Protocol/nolus-core.git
cd nolus-core
git checkout v0.2.2-store-fix

# Build binaries
make build

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.nolus/cosmovisor/upgrades/v0.2.2-store-fix/bin
mv target/release/nolusd $HOME/.nolus/cosmovisor/upgrades/v0.2.2-store-fix/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
