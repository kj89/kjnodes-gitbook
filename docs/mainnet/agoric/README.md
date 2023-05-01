# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/agoric.png" alt=""><figcaption></figcaption></figure>

Agoric is an interoperable Proof-of-Stake chain in the Cosmos ecosystem.  Agoric JavaScript smart contract platform enables 15M+ developers across the  globe to rapidly build and deploy dapps on-chain.

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoC | **Wasm**: OFF

[Website](https://agoric.com) | [Discord](https://discord.com/invite/qDW8DRes4s) | [Twitter](https://twitter.com/agoric)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/agoric/agoricvaloper1ku5sm2twlsywdrp4wz3kfwgyrtqtp0lpr3nvk8) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/agoric](https://explorer.kjnodes.com/agoric)

## Public endpoints

* api: [https://agoric.api.kjnodes.com](https://agoric.api.kjnodes.com)
* rpc: [https://agoric.rpc.kjnodes.com](https://agoric.rpc.kjnodes.com)
* grpc: agoric.grpc.kjnodes.com:127090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@agoric.rpc.kjnodes.com:127656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@agoric.rpc.kjnodes.com:127659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/agoric/addrbook.json > $HOME/.agoric/config/addrbook.json
```

**live-peers** (24)
```bash
peers="15f63de308337b66d8918ffaa74c6e956991bee9@138.201.120.161:28357,0464c8dded70d01f5ab50a8d6047a6b27ddf2ccd@84.244.95.232:26656,03c7d68a1433dde6db1acbbdf98712609843cc8f@161.97.187.189:36656,875f8b359148f0d2a4bb501f8ae8a0cd4560bff3@161.97.153.219:26656,9ed68bef54712b46713ac755ab7a6e7ad30694ef@192.99.44.79:14456,98d989f486d42ec75203f918495c420ca9665514@34.122.28.103:26656,37933cb8069e22554e454294d529eddb0fdae145@52.56.185.212:26656,81024f7597b22dd841613cac76a219d25a4533fe@13.215.217.74:26656,a38a30c1dd31f63be2befd40b82964b215c3c288@165.22.251.28:26656,63bd6649f80362ce513027d99ef32c826fdbd259@45.9.62.136:26656,711f6f36a6ec3924b6d721de6adce604092e59f2@116.202.226.169:26656,f095bb53006ebddcbbf29c8df70dddcba6419e36@142.93.145.13:26656,0837c0dac0bb15e79e64207bb0fa5a9a6fa42ad4@178.62.116.62:26656,0f642db2770d4dd3e0d030b2f14f1365e40f3b38@82.100.58.101:26657,1cbe5f5c77610bb6568332e026a3b516edeb0121@65.21.234.47:21156,8346a2f94b41b8f0d43c49e37ca2ffc9855936b7@34.28.102.95:26656,506f9bca6ce2f29a2556427f90693a8ee1b100ff@178.128.238.183:26060,ca4c3b9d0cf78d934a3b972c328db2e4a9a66c42@64.32.40.114:26656,d56af8cb0716909f9b804e7dec8c1d34ae4eed16@65.108.142.81:26676,e3f0b190cb101b0a33f7eefce4d088afd67905fb@35.193.203.105:26656,ebc272824924ea1a27ea3183dd0b9ba713494f83@195.3.220.135:27106,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:27656,9e673680df593d841b0e09c49f87409654d84ae9@95.217.202.49:37656,abc62ded9142361bd9832282242a53611785ffcd@51.81.109.109:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.agoric/config/config.toml
```
