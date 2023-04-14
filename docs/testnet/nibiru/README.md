# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-itn-1 | **Latest Version Tag**: v0.19.2 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: nibiru-testnet.grpc.kjnodes.com:39090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (28)
```bash
peers="391ce347a9f0745a1f50126fcc1f9a878bacd8fe@184.174.32.55:26656,0faa013496da308cf091099bb736f512f17ab380@185.144.99.55:26656,d2f53fd715b205d1321a22bad1a6334a06f3de2b@64.227.4.135:03656,4a44af55ee65d15c13d666bb5d830da43673f7a9@185.190.140.80:26656,2b67482054000c77f1db2f37072d20a6a1a043d4@194.163.174.35:26656,3bb1549a6b7536e673bb8b9a036485c5ec18ce76@194.34.232.36:39656,5b4b12ded2c0db5f29345580b507156ca5399053@31.220.84.69:26656,ba6a46ae8fe4e1e95c0debfa1d4f3012fa6b33af@66.94.123.46:26656,6b563f1f97557821d42ecaa234dc73266c28336d@173.212.234.123:26656,efc2e75111f286ca7117ce4e196bfb7ba29f0a5e@109.123.243.16:26656,abe0625166d3bc30612dde9c3863d7be2313316d@85.190.254.225:26656,b253cc6155ec59ea623f3f453d2f5a4b9c6d08fc@212.15.59.91:39656,766f17b24c11b5eac20cf938f619bc2e43331988@38.242.229.238:26656,59d4c5d5074043bf7ba617579a5120d6e0c97c39@34.30.210.193:26656,9ea5fbc168a099c75767aed80fe1dc8345f26b1a@185.216.75.223:26656,dfdfca675e009578b775d7febace9d15d97c3755@207.180.224.21:26656,17d683da420ce5eaa3fe1b9699b6b7720e4c5483@158.220.100.251:26656,15c155e1a3bc8a8004dbdc11c72399c8c5b08d74@212.86.102.214:26656,39ce82b6613c327f2bbc4cedc3a25dbf0bf8094e@38.242.252.137:26656,b02f28e0675743b077186b363386f10845c9e122@194.233.74.249:26656,6b76406fb872cc3a4d194c4f0910cf8893f6affb@38.242.148.145:26656,7bb000363922f1da93c0f25b2544e453b523a82a@65.108.246.178:26656,ecbf8f3be0826e9905dc0dfff5c02d922cf768b9@65.21.56.168:26656,d31e21c9ddc00e2ab2bbfbafde3810e2d4370993@31.220.94.117:39656,5d55ddb4d498af6062e6e7c0cb7a670aba9b3302@68.183.65.30:26656,e3bcf7faf6efca24f6d0735bc96f67929a8164d3@164.90.217.176:26656,65a213efcad697afb5a1303c7fe5be4168d9520c@43.154.103.36:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
