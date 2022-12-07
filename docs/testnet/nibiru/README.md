# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-testnet-1 | **Latest Version Tag**: v0.15.0 | **Wasm**: OFF

Website: [https://nibiru.fi](https://nibiru.fi)


## Public endpoints

* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)

## Peering

**state-sync**

```
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nibiru-testnet.rpc.kjnodes.com:39656
```

**seed-node**

```
3f472746f46493309650e5a033076689996c8881@nibiru-testnet.rpc.kjnodes.com:39659
```

**addrbook**
```
curl -Ls https://snapshots.kjnodes.com/nibiru-testnet/addrbook.json > $HOME/.nibid/config/addrbook.json
```

**live-peers** (10)
```
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,5c30c7e8240f2c4108822020ae95d7b5da727e54@65.108.75.107:19656,82cf00a5fc655cbb467b131d32e0305c46a87501@45.87.104.154:26656,1038f545b6495d29f1962fd72ba464d2277b85bb@194.5.152.252:26656,c9dcc45a1c3183f0df5751da6f5f7ae6f08138fd@188.134.69.27:26656,06a9ed460bc9bb592f6fe2e7c7545106d51dc729@176.124.220.25:36656,7cbdf8c9365b65353976e62cb3449a65ac973f1d@95.217.188.207:26656,5e65a3d32678a7206d006f899be707c130a9ada1@162.55.234.70:55356,fe6222472da3cfdb1d726f08ec148c43efbfefb2@173.249.59.70:33656,41c0720bd041ed4effc52a03c60cc821452ceb47@185.245.182.141:26656"
sed -i 's|^persistent_peers *=.*|persistent_peers = "'$peers'"|' $HOME/.nibid/config/config.toml
```
