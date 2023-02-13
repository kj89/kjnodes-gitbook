# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nibiru.png" width="150" alt=""><figcaption></figcaption></figure>

Nibiru is a sovereign proof-of-stake blockchain, open-source platform,  and member of a family of interconnected blockchains that comprise the Cosmos Ecosystem.

**Chain ID**: nibiru-testnet-2 | **Latest Version Tag**: v0.16.3 | **Wasm**: OFF

[Website](https://nibiru.fi) | [Discord](https://discord.gg/nibiru) | [Twitter](https://twitter.com/NibiruChain)




## Chain explorer
[https://explorer.kjnodes.com/nibiru-testnet](https://explorer.kjnodes.com/nibiru-testnet)

## Public endpoints

* api: [https://nibiru-testnet.api.kjnodes.com](https://nibiru-testnet.api.kjnodes.com)
* rpc: [https://nibiru-testnet.rpc.kjnodes.com](https://nibiru-testnet.rpc.kjnodes.com)
* grpc: [https://nibiru-testnet.grpc.kjnodes.com](https://nibiru-testnet.grpc.kjnodes.com)

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

**live-peers** (33)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:39656,92845d4150aaf87fc1a6f4a53d8fe545ae44fc9d@86.48.16.205:39656,3939da5da8d8a31e6af2cb6d7bdcb222ff2487eb@65.109.14.69:39656,d7185d6b0d6a7dbe8c45e1fddfa0165dfdba01c0@38.242.150.132:39656,e55d8746ad30e0d11ebe0aa3792c46713375edcc@135.181.2.104:26656,aa3261d279f300aad20cb30262c910884c3a5b05@178.20.41.240:26656,64d7ce7fda6c229bba3952c097a26f64740a4cd3@164.92.136.155:26656,cf29df0bc1d8a1d9053d7dc6bd7b8ee69b3021cc@51.89.47.31:26656,efb2dd9cf401c6c1a97fda94183d52c5000ae8e9@38.242.252.157:26656,f4548f7cdc44905740f1a28c1ba0c68ca393eb8a@95.216.163.41:39656,a575313137ddc0dae09fc79ad5558f2ca25867af@199.175.98.114:26656,b57a9c1e7c0f597c9ef6a47cc361094f95a22b84@192.9.134.157:27656,10c9aecb4f414d45863cbe1a5f91d04b33fcb638@80.85.242.54:16656,17d7a3d370413dc134b5f24fff475d78213570ad@207.180.236.124:26656,a4a0b5b90dbcc92006e7d05d7f6521f120520116@34.75.178.18:26656,aeefeab21ebc6913e91d9ca81ae240f691720cd7@142.132.186.213:26656,3a88426d413c9f7794485bdeab5e1cfda1c7430f@77.232.43.194:26656,80030d5945eef7519407d047479d40a2f2bf1fe6@65.109.92.241:11036,9e05e4a15d6077088cbd84fa5a4311e71556e67a@62.141.37.231:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.140:27046,63903e6cc8e3c8dd2144caaa7d0249edf526148d@38.242.142.76:39656,fe5a3ffcbf6d5958a107ba1e5e8497096b98b863@75.119.153.120:39656,3cdff6866538896ae44acf5d644b201242483619@89.117.54.230:26656,780a0beff082046c143a9c110f66078e2154c22c@94.130.137.122:28656,e63604bb6323eaafb02a72cb825d770fd7f1998c@65.109.70.23:19856,0a603e47f24252b2a96d734913f83190c9627f45@46.4.50.247:39656,ce5f1c19251113d7cf8cb73a71cf524bccc08e0e@94.130.38.122:39656,6df779cceccc7468ceb001ddbd2167471838ca61@149.102.158.241:26656,b28b1488f769acc32d7f4a9dae1d9b4e1d6ba2b8@138.201.53.44:26656,9e4cbbf1ae74859df3a4f1a3579bb52b09ce26f0@167.86.76.166:26656,82b5aadfb42e471af43c916d27dbaa2aa28c0bf8@109.123.247.230:26656,6b79cd4cadd1590367ff87311d87a1eec0491b6f@212.86.102.214:26656,9920bfdee1f9f61221e0301b1823f050e8fb992f@193.203.203.121:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nibid/config/config.toml
```
