# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.3.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

[![Stake with kjnodes](https://i.ibb.co/cr44Q8j/button-stake-with-kjnodes.png)](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv)

Subscribe to our free [🤖 Mainnet Proposal Bot](https://t.me/kjnodes_proposal_bot) to never miss upcoming proposals

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every 5 minutes)
## Chain explorer
[https://explorer.kjnodes.com/rebus](https://explorer.kjnodes.com/rebus)

## Public endpoints

* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)
* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* grpc: rebus.grpc.kjnodes.com:21090

## Peering

**state-sync**

```text
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@rebus.rpc.kjnodes.com:21656
```

**seed-node**

```text
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@rebus.rpc.kjnodes.com:21659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/rebus/addrbook.json > $HOME/.rebusd/config/addrbook.json
```

**live-peers** (20)
```bash
peers="f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,ebc4d27be0c87f537b44250c2e22ad349dc59fb6@158.69.116.134:26656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,faf349e185255c4aa2786da4f8ac70ea13849db0@169.155.45.128:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,c124ce0b508e8b9ed1c5b6957f362225659b5343@134.65.192.98:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,e772ebf24c2fda82456812050fee31e19c9455fc@65.109.122.105:61456,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,69e27ab9b46350654805df3ea8d9ac2f00af4e4c@38.242.244.85:26656,30ff8100fefac53ee40ef7631f1a3c66ca2b82cf@135.181.164.90:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.rebusd/config/config.toml
```
