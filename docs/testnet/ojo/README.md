# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" width="150" alt=""><figcaption></figcaption></figure>

Ojo is a decentralized security-first oracle network built  to support the Cosmos Ecosystem. Ojo will source price data  from a diverse catalog of on and off-chain sources and use  advanced security mechanisms to guarantee the integrity of the data it provides.

**Chain ID**: ojo-devnet | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://ojo.network) | [Discord](https://discord.gg/fd8Yrex8nC) | [Twitter](https://twitter.com/ojo_network)




## Chain explorer
[https://explorer.kjnodes.com/ojo-testnet](https://explorer.kjnodes.com/ojo-testnet)

## Public endpoints

* api: [https://ojo-testnet.api.kjnodes.com](https://ojo-testnet.api.kjnodes.com)
* rpc: [https://ojo-testnet.rpc.kjnodes.com](https://ojo-testnet.rpc.kjnodes.com)
* grpc: ojo-testnet.grpc.kjnodes.com:50090

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@ojo-testnet.rpc.kjnodes.com:50656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@ojo-testnet.rpc.kjnodes.com:50659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/ojo-testnet/addrbook.json > $HOME/.ojo/config/addrbook.json
```

**live-peers** (41)
```bash
peers="3cd8b55fbb2c4e87ee5e39554155051d0d98edc4@188.34.187.252:50656,a9bcb95ee047c4a909c675dc36c556eafe1248e1@195.201.174.109:46656,50ad0e558d9da6fce98ae4527cd49ee3e8d19940@94.250.202.215:26656,ea0ad608f0fa47e20047569c7c0c1ff76dd3d724@45.151.123.72:28656,340f0623e9338a5c93baf2d8a8825718a86d3e8b@195.3.223.196:26656,62fa77951a7c8f323c0499fff716cd86932d8996@65.108.199.36:24214,408ee86160af26ee7204d220498e80638f7874f4@161.97.109.47:38656,9ebe723eef929e9eff748f4046d6130ee349a398@65.108.203.149:24017,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,d5b2ae8815b09a30ab253957f7eca052dde3101d@65.108.9.164:24656,3c6384ae2a167912a5ace2f5f8e38afc559715f0@75.119.156.88:26656,4bfc6d62d115a2440f9e5dc10c21d302dbdf5c64@34.220.136.165:26656,b6b4a4c720c4b4a191f0c5583cc298b545c330df@65.109.28.219:21656,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,8b6c75d20ac3ceeb7f0f1d4b5fc89a69e567c47b@65.108.231.238:36656,4764a447ea3518e5017756b42ca5f6442b2f5768@5.161.114.1:26656,969b1e53d217abf769054777190f9a65eb8174cf@46.4.61.91:26656,863a266ca1a958b9d122511289041905120e26dd@185.245.183.254:26656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,67e95aeec46d7c5840f9685ca2b4cd725841b814@16.163.74.176:26636,0621bb73d18724cae4eb411e6b96765f95a3345e@178.63.8.245:61356,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,f4663c5df8ee2e2b6e1cc6a9d7ad09687a27e08c@68.183.32.158:26656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,23830179727e6e38933e95000cb84ece4112f78c@185.155.97.74:18656,b0968b57bcb5e527230ef3cfa3f65d5f1e4647dd@35.212.224.95:26656,1c69ce0386cf66825a906a6b91bc55fcd5924f8b@194.233.89.251:50656,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,f702b19a4dae5ad813dabe3f529bf31c160a74e0@5.189.176.202:26656,1e2a49792b0e0686827ec0fbc101a9ad709e0f28@88.210.9.78:26656,8ee9b08d75823b13ca5517c3469f6aaf541aa684@65.108.43.58:27675,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,1b5c5927e6e3685b3e9fc278ca4c9d7002d4cc10@65.21.134.250:26656,d7dbc0d436536945b7bd6254c1bedfebbf3e586b@65.109.88.254:47656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:26656,9aa8a73ea9364aa3cf7806d4dd25b6aed88d8152@190.2.136.144:11556"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
