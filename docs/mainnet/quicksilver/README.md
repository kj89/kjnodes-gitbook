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
peers="f73b2b887e7d1c01a3d753db359a0058e634e767@65.108.201.154:2090,a4f29a68180d1a1c931b50e2438a63b0d45d6915@89.58.48.229:26656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,e64a4e480a2971c339fa06a58293e8e060082ad5@185.16.36.134:26656,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,bdbb005129890e3b656841415b3b728d1e4529e6@142.132.138.18:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,f736b49c260e11d3f81a5d99814eaeda396c1597@18.138.35.164:26656,1c3db399f804a111efebeeffb5cdc4e751fb8108@65.109.61.113:21609,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,34047b39deae3110158c2bf7359e4a1b559dd8ca@159.89.171.207:26656,0865ef3e5a613f75f17a0092bd47e71d8c171124@51.222.44.116:15656,c8b01e6700d048b1aae34d76f5c56511b2a90ab1@57.128.133.24:26656,c2a44958de52a8656eba9eedaf88205f27686ffd@46.4.23.42:11656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,8a0740d4b70629c26022db7525132da0062bf42b@194.62.99.114:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,41caa4106f68977e3a5123e56f57934a2d34a1c1@185.16.39.137:27026,cc091c4d385e449a718fb252de800a9caf01913f@95.217.225.212:11656,149a25417349d70f5e5127a5eb634dbfaf6e6c3a@142.165.207.19:56656,b4bcce87121963e1e97619dc135f2eb1a9fd5dfc@88.198.32.17:36656,04dcb466b6804e6a57b7f9188b90f5bdc17037c0@108.165.178.242:26654,d2517139cf7c20ebdad682dfaeb2c34822a255b6@31.223.32.35:19656,a87f48e433160970318d181bb69c378f4564cd2d@107.155.67.202:26736,995fcd08f3423266338effe441804a5490a728a7@37.59.21.96:11156,161f453c9ff27f3120ec5078f56b505316fbc720@65.108.6.45:61156"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
