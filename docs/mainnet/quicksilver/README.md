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
* grpc: quicksilver.grpc.kjnodes.com:11190

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@quicksilver.rpc.kjnodes.com:11156
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@quicksilver.rpc.kjnodes.com:11159
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/quicksilver/addrbook.json > $HOME/.quicksilverd/config/addrbook.json
```

**live-peers** (30)
```bash
peers="51070ba609ede6d7eb334b8cf0ed585f2b1ab66b@135.181.76.99:26656,71b753819eb653e99e6a825b80af20ca9bccb087@135.125.163.63:24666,cdd8e0e425f107d249389a5e4cea3494185d4a3a@193.70.45.106:11156,3a5d0b97feb595375c24665dcf17d793be129e8b@51.89.155.2:28656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,46a0c8717148c4a4aa86eaaa9727e7bc6bb8e70c@49.12.7.7:26656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,d0c81152bc586896c6c2a4dba15a4351742768d2@65.109.90.169:46656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,f736b49c260e11d3f81a5d99814eaeda396c1597@18.138.35.164:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,0521c200a3dc430927978fb2c66293b8481fc3ae@198.244.203.181:26656,4de2811fd20d33110daf62223975beccecbe55a0@15.235.114.195:26656,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,50a40c5aba326798ea9520ac0a1207e22a540a0e@95.214.55.100:26556,71f722098fc28c2f39026af58d539f387451ddb0@65.109.86.210:27656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,0865ef3e5a613f75f17a0092bd47e71d8c171124@51.222.44.116:15656,161f453c9ff27f3120ec5078f56b505316fbc720@65.108.6.45:61156,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,e72108879602113f6661507b583ff8b5616f06c6@95.217.202.49:31656,d2517139cf7c20ebdad682dfaeb2c34822a255b6@31.223.32.35:19656,cc091c4d385e449a718fb252de800a9caf01913f@95.217.225.212:11656,9bed2c944243fd3ee35a6e4e8da0956f61518603@65.109.19.176:26656,0ad45ecd219b9151ac17951dc1cd6303bcda2b58@65.109.106.169:26656,995fcd08f3423266338effe441804a5490a728a7@37.59.21.96:11156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
