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
peers="641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,4e2a874e538319f204f03751a5e458d0371d5b92@65.108.98.125:60556,256d9790bf186f5a275790f7fe01e1b8800dcaaf@65.21.88.78:26656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,4a4d2e7070e05ad6c13628d2f191d96172659452@65.109.65.210:40656,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,ff7031f45a97600076f72b9318167e3dfcd2a17e@65.21.136.170:52656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,404ae118865c1485f7859fa2c7cc2e3b8c402a14@51.75.135.34:26656,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,a3d975c913570ad217d9a3de01a8616ad5ce20f8@142.132.128.137:26656,5a13200e67f6cb5385d9d8f8c68a7b5e62f8cd54@188.34.176.96:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,2b7c9ae046c35b48cb7d3d16416c3f36ab648f66@149.102.136.149:26656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,6daeb8cfea285f561e167a0d94718b61e2cf7944@5.189.187.36:21656,3e319c765b7b48d518a2e3218efc317234b81681@142.132.159.188:26656,1e19e8668693863bf573c61f1a83523bf661f9ad@38.242.242.99:26656,b212d5740b2e11e54f56b072dc13b6134650cfb5@169.155.168.16:26656,89ded0a3987d22e46b756fead439e2a4d25f23cb@185.144.99.30:26656,6ac55af662061d3669d7c70961a8fd87ba2f2075@65.108.200.142:26696,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,c126eed9cfede7802d78f570fec8175835309a73@141.95.127.146:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,0863966356f6532377aeba663415258d44ddbd13@88.99.164.158:40106"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
