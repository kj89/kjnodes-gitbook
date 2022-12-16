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
peers="1fcb45323f9045707c0c344a60d7cb906008cfaf@65.109.80.176:26656,f2483e5af4cb1fab55e4f6422627c0365f45b5dd@194.163.188.252:26656,a35d28e111c1dcc1e5f3203627b449adfb4425f2@65.109.29.150:21656,9d17d1c5b5d3b8c9e7ffab264b45b5dd979116f3@65.109.24.188:26656,e056318da91e77585f496333040e00e12f6941d1@51.83.97.166:26656,3a378fbfae33a593b913371c876c9d275c0abb12@213.239.215.77:26656,235a2754b94c86a85ba645119151ee55d6971554@213.239.216.252:26656,0fedf7695d9e2721663c1d573d6d81a14c21533e@65.21.90.137:12856,1fe32d8f09b8715b1e626da17b3ecfe26623b371@176.9.22.117:27656,641b33b0e909630868133820605edf2b4ba4969a@65.109.49.109:26656,cd71aa366822800a2aa7051fae69127f78b3f203@188.165.225.226:26656,2f6b34ad97c4827dace87436f0299cf89fe0c056@136.243.95.80:46656,b1b08fe470551dca6d6631fb1bfabb814f6c1aec@54.37.129.164:54556,f546370843f92e2415524a7b18f9cd528e2fd706@65.109.55.186:26656,34e3178b6e0f25451fd690c15fc199d5a9bdfb9b@15.204.197.11:26656,b1dcbb37514fbe215be54079e71aa39dac7fd0ae@64.5.123.203:26656,18ec83c4e3938aec31a3a32154969107739f0b81@135.181.153.228:26656,f467e286567f94c89d39a5bcea0e1d68951299f9@146.59.81.204:34456,92245ff5c7a4b293d2f0c7f9afca0ddad2e0fb52@65.108.244.178:26656,b570827e4397512e077028ea7121d3e19eb25bab@85.10.200.221:26656,056d6a61c8a4c5ccb02123d67a013434423f155a@149.102.142.57:26656,5c2018214fcfde67ec390702539f295165f12a3a@86.48.2.20:26656,b8ed7daa4e2966f6c160915600d7dadf7e3ef61e@62.171.142.94:26156,ce38728ac38ebbb4a72d496d42f8e9030af441d7@162.19.137.25:26656,bb2a7dc81b9bd0e017409a2bbb71b12bb899e743@178.63.22.117:26656,ab6a4ae2857ac05fa8f45b03871fa3945193fc61@46.4.81.204:35656,fa292bfad37826c9da43894b349b1480dff516b5@65.108.99.254:31656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:21656,304ff8e051b2fbd038771142b69ac915c14c0819@78.46.78.83:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.rebusd/config/config.toml
```
