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

**live-peers** (29)
```bash
peers="b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.98:26656,c764a288f1d36e7ca2c953378bb4fd6a0eed4091@141.95.65.73:11156,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,5f0c0411e34e1c7d0b9c53749d90a923b5e8c625@65.21.133.125:35656,d11e03ee30496ef827383d5dcbbc55e7b3171189@35.240.184.52:26656,71b753819eb653e99e6a825b80af20ca9bccb087@135.125.163.63:24666,28ebd43e8c888ed069165fa035e101ae6fd7955e@139.162.191.246:26656,625eeb91fcc6242798f53426540825e5b37c7670@185.144.99.16:36656,cb6ae22e1e89d029c55f2cb400b0caa19cbe5523@172.111.52.50:32662,2020c09ef7542899a4c55b382013c469122186d6@51.195.88.136:15620,ff2055b198685f619897058a26776b9d1b73dc3c@178.63.184.129:26656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,cdd8e0e425f107d249389a5e4cea3494185d4a3a@193.70.45.106:11156,ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,06230bbaabb6c9c6223275b57d8e10fc609ae7ba@51.89.7.184:26633,443ad7c991b2915b620673b10206c92e2b4040e0@173.67.177.120:26656,26d23125db7493486dc9931b4181425d725e4ac6@65.109.55.186:20656,46a0c8717148c4a4aa86eaaa9727e7bc6bb8e70c@49.12.7.7:26656,8ebd6e7c74a9c36a175f9a86148354b378a4f387@185.248.24.16:26656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,36640aca1c3109ef36d607ec650e8eff832bb39c@195.14.6.2:26656,67c3cc1397d0a0f03a45d4cae6ff3380be7364f9@95.217.229.18:11656,d057145a457f3e3565926d3b385acd366f117d18@65.109.52.178:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
