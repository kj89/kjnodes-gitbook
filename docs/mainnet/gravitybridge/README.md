# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/gravitybridge.png" width="150" alt=""><figcaption></figcaption></figure>

An open, decentralized bridge that unlocks the power of  interoperability & liquidity between blockchain ecosystems.

**Chain ID**: gravity-bridge-3 | **Latest Binary Version**: v1.7.2 | **Wasm**: OFF

Website: [https://www.gravitybridge.net](https://www.gravitybridge.net)

## Restake

[Restake with kjnodes](https://restake.app/gravitybridge/gravityvaloper1nw3uavthnjwsgrrjzav2wdg9m0pw7k4fc7hvlz) (every day at 08:00, 20:00)
## Public endpoints

* rpc: [https://gravitybridge.rpc.kjnodes.com](https://gravitybridge.rpc.kjnodes.com)
* api: [https://gravitybridge.api.kjnodes.com](https://gravitybridge.api.kjnodes.com)

## Peering

**state-sync**

```
d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@gravitybridge.rpc.kjnodes.com:26656
```

**seed-node**

```
400f3d9e30b69e78a7fb891f60d76fa3c73f0ecc@gravitybridge.rpc.kjnodes.com:26659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/gravitybridge/addrbook.json > $HOME/.gravity/config/addrbook.json
```

**live-peers** (10)
```
peers="fec4e193084be7321794246cf50887b1b91c6664@65.108.74.176:26656,2acf8add94531707982f17b91192866ad02de504@154.12.227.186:26656,a2b2723dffd2dc3a8e5ea727f60c3eca3a07c6f5@80.64.208.80:26656,930f874c17eff988acd8eb761fea8d4873ea6eb3@185.249.227.231:29656,1643554bc52ec036f0f81aa72db14a4a0089d554@195.3.220.169:26656,d9bfa29e0cf9c4ce0cc9c26d98e5d97228f93b0b@65.109.88.38:26656,91e4523f2fcf6c7a8314b583d2f9f92cf93f10d7@51.250.18.132:26656,da401c011881747aa47b7348349edfc855794ba2@74.208.108.68:26656,4bebde6a1b2907bd3cc167d2802b909770cbfda1@137.184.197.230:26656,c4385ec685f08dfd635df6d21be9dfbdfdb52896@161.97.182.71:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.gravity/config/config.toml
```
