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
peers="6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,5f29f14fe3dd7e1d86caa4d344e67ee81c32255f@65.109.37.228:26656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,dda7abe32cc84a722cf6b1d2ee3b61ebe7ad71df@135.181.212.183:21656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,404ae118865c1485f7859fa2c7cc2e3b8c402a14@51.75.135.34:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,235a2754b94c86a85ba645119151ee55d6971554@213.239.216.252:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,5a13200e67f6cb5385d9d8f8c68a7b5e62f8cd54@188.34.176.96:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,07b84cf4b47a2e5ad251267716fe05bcf30330cd@65.21.170.3:29656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,f467e286567f94c89d39a5bcea0e1d68951299f9@146.59.81.204:34456,b8c42fcb311b47cdb8285b5697f661fbba5bf1a5@51.68.157.129:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
