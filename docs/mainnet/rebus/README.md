# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

[Website](https://www.rebuschain.com) | [Discord](https://discord.gg/rebuschain) | [Twitter](https://twitter.com/RebusChain)

## Restake

[Restake with kjnodes](https://restake.app/rebus/rebusvaloper1vndzy8y55ylgpmmsc34uy8rm6kqlml6ffs9lrv) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://rebus.rpc.kjnodes.com](https://rebus.rpc.kjnodes.com)
* api: [https://rebus.api.kjnodes.com](https://rebus.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@rebus.rpc.kjnodes.com:21656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@rebus.rpc.kjnodes.com:21659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/rebus/addrbook.json > $HOME/.rebusd/config/addrbook.json
```

**live-peers** (30)
```
peers="1f7c31506f465c5f5536862074e98fc7a6043d4c@65.108.13.212:26656,4e2a874e538319f204f03751a5e458d0371d5b92@65.108.98.125:60556,3a3e7123b9ae814b8d8517b6635d21b9ae45bf25@195.3.222.148:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,5a13200e67f6cb5385d9d8f8c68a7b5e62f8cd54@188.34.176.96:26656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,f467e286567f94c89d39a5bcea0e1d68951299f9@146.59.81.204:34456,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,170397e75ca2b0f4e9f3b1bb5d0d23f9b10f01c7@94.23.23.189:30544,1e19e8668693863bf573c61f1a83523bf661f9ad@38.242.242.99:26656,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,09d22b9fc1b07f3e2f64b685ab6f28130bc2edd2@51.89.7.185:26637,b8ed7daa4e2966f6c160915600d7dadf7e3ef61e@62.171.142.94:26156,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,b5bf2242c981371224e5e9e89d6c265d554c8989@65.21.202.154:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,b574e11e103058a121cc03d1c4d9867ba3daed34@135.181.139.113:31656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
