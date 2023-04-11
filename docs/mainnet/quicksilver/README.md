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

**live-peers** (28)
```bash
peers="61d96fee29a9615c208c4db72526d23b45094cb4@65.108.195.30:36656,71b753819eb653e99e6a825b80af20ca9bccb087@135.125.163.63:24666,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.12:26656,e64a4e480a2971c339fa06a58293e8e060082ad5@185.16.36.134:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,618e09601dd5abb2bd02de957982742e4c1975ab@195.14.6.2:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,d057145a457f3e3565926d3b385acd366f117d18@65.109.52.178:26656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,0a226e70ceb7a4123e66216d1ed83ef22ed8a187@185.119.118.118:2000,ebafaa0d0087ecfc785b095d6a91a67a12eecd80@5.9.100.25:26656,cbc2c7a7cd39750abee0dcd5dd2832feddbde20e@50.21.173.76:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,185f80586290dcd53db67ebc2da1e146e291bcd6@148.251.13.186:11156,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,d5a9c9ae08f0d30e36c8f64eca046fc52b00561e@65.109.92.160:26656,e1a24aaba30a8ff21e52fed92b96b36156b52e80@51.161.208.88:26656,ec076ff33f2986d064b78602e2ccd2c925bf761e@161.97.82.203:26256,ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,ae353518e6009eb48d80ccf6a006a9644e9dd309@146.19.24.101:26656,7f7905d479080999dea84fd479ab0df6e4069de3@146.59.118.31:32182,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,ce593f9bffc471ba4b980a435a3e2f8eaa5b464e@35.198.80.195:26656,3b3c0037090a1b5ef9f7ac58ff79f33dffdd188a@65.108.231.124:15656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
