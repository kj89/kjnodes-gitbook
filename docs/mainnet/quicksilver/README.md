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
peers="914bed178748772d7578d119cb2dc89d5076b9f4@135.181.223.115:2390,f73b2b887e7d1c01a3d753db359a0058e634e767@65.108.201.154:2090,c764a288f1d36e7ca2c953378bb4fd6a0eed4091@141.95.65.73:11156,bbb6a02a90ef98975525d9bd7137511e18edddc1@141.95.99.81:26656,679f56feb7f4f91d46a92d0eb474d1dc43466d18@213.239.215.59:29986,271419d3eb3878c902ebb0064490ad702d9d067f@144.76.145.150:26656,225a08945298003a397eb6a51854525948fd9a5b@162.55.245.149:2010,9bd2b7e39fb0d823402f22c90e3000fdf3cd05bf@88.99.104.180:26656,602700ce2ed57b2176514ec2ecbda079caa7a536@178.170.40.28:15620,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:11656,0a226e70ceb7a4123e66216d1ed83ef22ed8a187@185.119.118.118:2000,ef1cb5bff5b76957f02636a30d5d85d861a35dbe@65.109.92.240:21026,3bd869c02bd787d7bcc3b7059364608fc4e44620@141.94.202.185:32306,d057145a457f3e3565926d3b385acd366f117d18@65.109.52.178:26656,e3dd956ac4081ba42ae3d038edd6d80ddf092751@198.199.90.99:26656,f73ee3d2450f41bcf1b2975552cdf60a118a64c9@46.4.50.247:11656,c3ec2daba16e457ca5117079f34ff49e99e7572d@65.109.94.221:35656,6785dbb8a0138600e0e0faaa77baa375451b38bb@162.55.132.48:15620,618e09601dd5abb2bd02de957982742e4c1975ab@195.14.6.2:26656,e726816f42831689eab9378d5d577f1d06d25716@176.9.188.21:26656,c05c72b90e5a3d80f67e9da884a3f97b884d8ac2@65.109.112.29:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.136:27026,3bd708547317e9efd8d63d8a51c5bc32d11f4840@138.201.32.103:26056,e09b47db9c221a9d064069befcc471d949d2c28d@45.14.135.159:15620,3394976851c8a06002989572119925f6d839a980@51.195.234.250:26656,c8b01e6700d048b1aae34d76f5c56511b2a90ab1@57.128.133.24:26656,c0beca70dbd3ef5bb433f7aa280d56d2a150bbd3@95.214.52.144:26656,3a5d0b97feb595375c24665dcf17d793be129e8b@51.89.155.2:28656,a57b371b2bfcebafddf95daa34b69a4d55d38931@77.241.194.52:26656,3b3c0037090a1b5ef9f7ac58ff79f33dffdd188a@65.108.231.124:15656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.quicksilverd/config/config.toml
```
