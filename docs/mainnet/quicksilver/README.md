# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" alt=""><figcaption></figcaption></figure>

Quicksilver is a permissionless, sovereign Cosmos SDK zone providing liquid staking for the entire Cosmos Ecosystem.

**Chain ID**: quicksilver-2 | **Latest Version Tag**: v1.2.9-hotfix.0 | **Wasm**: OFF

[Website](https://quicksilver.zone) | [Discord](https://discord.gg/quicksilverprotocol) | [Twitter](https://twitter.com/quicksilverzone)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/quicksilver/quickvaloper1fqfgpwdngmmay6ah7mg9y4k7ayykpzu6l3ht2m) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/quicksilver](https://explorer.kjnodes.com/quicksilver)

## Public endpoints

* api: [https://quicksilver.api.kjnodes.com](https://quicksilver.api.kjnodes.com)
* rpc: [https://quicksilver.rpc.kjnodes.com](https://quicksilver.rpc.kjnodes.com)
* grpc: quicksilver.grpc.kjnodes.com:11090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quicksilver.rpc.kjnodes.com:11656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quicksilver.rpc.kjnodes.com:11659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (28)
```bash
peers="ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,4de2811fd20d33110daf62223975beccecbe55a0@15.235.114.195:26656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,914bed178748772d7578d119cb2dc89d5076b9f4@135.181.223.115:2390,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,149a25417349d70f5e5127a5eb634dbfaf6e6c3a@142.165.207.19:56656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,f736b49c260e11d3f81a5d99814eaeda396c1597@18.138.35.164:26656,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,697d2a513d46edaa2bec82992fe1a8c4d03e4684@1.15.117.20:26656,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,4aa6607f87ad0b458526d3405731e71553cf275c@219.100.163.35:26656,3308d9078fcca016fbd8dc8f3b19666326f41a6f@138.201.121.185:26672,34047b39deae3110158c2bf7359e4a1b559dd8ca@159.89.171.207:26656,04dcb466b6804e6a57b7f9188b90f5bdc17037c0@108.165.178.242:26654,cdd8e0e425f107d249389a5e4cea3494185d4a3a@193.70.45.106:11156,040c3f32308aa75fa0f4d3b1b7c88ab5d45058a9@65.109.19.176:26656,41caa4106f68977e3a5123e56f57934a2d34a1c1@185.16.39.137:27026,0865ef3e5a613f75f17a0092bd47e71d8c171124@51.222.44.116:15656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
