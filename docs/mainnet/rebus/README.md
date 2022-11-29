# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/rebus.png" width="150" alt=""><figcaption></figcaption></figure>

Rebuschain is a platform that will provide DeFi (Decentralized Finance)  investment opportunities to traditional investors clearly and conveniently

**Chain ID**: reb_1111-1 | **Latest Version Tag**: v0.2.0 | **Wasm**: OFF

Website: [https://www.rebuschain.com](https://www.rebuschain.com)

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

**live-peers** (29)
```
peers="1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,d241f395a167fd7a9f155641760bffa8af6a50d2@167.235.98.202:27656,346bf012c17fa30ef70ae72f082374838626532a@65.108.106.131:26696,f97a11f283cd5f11bf1fe73d8b2012b711d61ce9@38.242.205.80:21656,12703ce9efe6c1171c193dae2e2041a2be610852@65.108.44.149:29656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,15b1c913dc3d9dab7c912b27bb2a957abbfe8834@142.132.199.27:40106,6d8c83cc702365363b829a14efdd414401da369b@23.88.69.167:27565,b8137c688096d1abcf56942d335d061f212e6629@62.212.65.138:34656,d6c891779edb84d91aa7dd043dcc819c11bf6895@185.245.183.106:26656,40e2c0b68a1dd48466714e3dd0581e4b7d498575@107.155.122.93:26656,237bfc05da5f8cabee00f148995333f37186d232@164.68.121.101:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,f2483e5af4cb1fab55e4f6422627c0365f45b5dd@194.163.188.252:26656,3cc5fb5f6140ac4e57dfc80940c8a06daa299c89@51.77.195.46:26656,eeca453e3a1cf670c78e2255b8f0bd5a9443c30b@65.108.225.71:26656,36afb1c827f52d38d7cd328b384d644b531b5997@65.108.238.102:17256,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,77ca73199cf0a73ab52fc216d8ab8f8756275fef@138.201.8.248:52656,b8ed7daa4e2966f6c160915600d7dadf7e3ef61e@62.171.142.94:26156,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,d28516746773bfaeca4efa5537c0bf5990b8828e@65.21.229.33:27656,6ad5dd14c578016cc7bc4d7c6d6f7f773bba39af@65.109.60.57:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
