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
* grpc: [https://ojo-testnet.grpc.kjnodes.com](https://ojo-testnet.grpc.kjnodes.com)

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

**live-peers** (39)
```bash
peers="9f53e51449968bb2d2faad15dc4220757c4c33cd@213.239.215.77:47656,97a388be825fc69fca40a8a3de75aa5794602abb@95.217.225.212:36656,8e69c82fd42041a5eff49bcb94ae65c037aa45a9@65.109.87.88:26156,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,f4663c5df8ee2e2b6e1cc6a9d7ad09687a27e08c@68.183.32.158:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,edfbe6f29c7fbaec27d68d0d9fa83ca0ee0eaa71@143.198.181.190:26656,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,f35a6ea4693d24d3727a8e866acab2a9faa2ddbc@91.223.3.144:26256,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,b0968b57bcb5e527230ef3cfa3f65d5f1e4647dd@35.212.224.95:26656,ca46b2279f09daf8e89a8571ad1ccb3f8e6d0463@185.15.244.245:50656,5a36595613f189a3c1096729897fb02be0a8c15e@89.117.50.187:28656,f702b19a4dae5ad813dabe3f529bf31c160a74e0@5.189.176.202:26656,50e9bd8647571268df2313df6c46ba9960c9f40e@178.128.88.30:26656,4764a447ea3518e5017756b42ca5f6442b2f5768@5.161.114.1:26656,1879aa588b4d6431bf40543f3a44129dcf60a043@144.91.77.68:50656,9aeb9250f279c9e288b7db702380e2970a36e248@5.188.118.105:46656,0621bb73d18724cae4eb411e6b96765f95a3345e@178.63.8.245:61356,9dc1f555bd37d6840237f32a2cd4d79ba1c80cb5@65.108.227.112:31656,4609153f2b095b6c7f98b9cd3d079fe8fcd992db@95.216.14.58:61356,5acc5ccc09dc10f5bc12c4ba4468a03c3df9d1ea@65.108.8.28:61356,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,323d4309091003ea96ec3076b8bf4dc319c71345@109.205.182.137:26656,3832f6d02addadfe4acfbd1a87ccc009642a348e@195.46.165.3:26656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,91eba8f362b6c41d324ff26f316ce0b50d22b955@213.136.84.176:10656,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,67e95aeec46d7c5840f9685ca2b4cd725841b814@16.163.74.176:26636,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,5c82e32c31d85949086bb86b94c782595715c133@195.231.85.144:28656,b6b4a4c720c4b4a191f0c5583cc298b545c330df@65.109.28.219:21656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,3c6384ae2a167912a5ace2f5f8e38afc559715f0@75.119.156.88:26656,8ee9b08d75823b13ca5517c3469f6aaf541aa684@65.108.43.58:27675,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
