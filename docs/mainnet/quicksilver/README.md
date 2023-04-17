# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/quicksilver.png" width="150" alt=""><figcaption></figcaption></figure>

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

**live-peers** (30)
```bash
peers="51070ba609ede6d7eb334b8cf0ed585f2b1ab66b@135.181.76.99:26656,841efbdd6cd5c7191b5ec849499dfd9d1ea6a931@23.88.69.22:28566,ff2055b198685f619897058a26776b9d1b73dc3c@178.63.184.129:26656,b71ddbe0702383c73128f759a910a6d55ccee3b6@46.4.112.18:11656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,06230bbaabb6c9c6223275b57d8e10fc609ae7ba@51.89.7.184:26633,e72108879602113f6661507b583ff8b5616f06c6@95.217.202.49:31656,bdbb005129890e3b656841415b3b728d1e4529e6@176.9.155.98:26656,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,58fcbfdb3568a7059d9b46eb98ee9c1e4768c049@217.160.148.161:26656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,0865ef3e5a613f75f17a0092bd47e71d8c171124@51.222.44.116:15656,b00a1e8869d0a8327f12f12d6b63bacf15527525@213.239.207.175:32656,ce3837aa07eb0967c024d4c592f7c2730754bdd8@157.90.179.182:26656,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,6f80fa3110d45fa7cf08fe7df94cf9f60da8ad4a@178.63.67.112:26656,7b5fc2dfe1ca54840bd1ea7c332a7516d8ae772f@65.108.130.171:26656,34047b39deae3110158c2bf7359e4a1b559dd8ca@159.89.171.207:26656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
