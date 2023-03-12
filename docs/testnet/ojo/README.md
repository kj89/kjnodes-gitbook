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

**live-peers** (29)
```bash
peers="978cf9aca38f819fd8189272379fc3c2ae2682a8@213.239.218.210:56656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,f4663c5df8ee2e2b6e1cc6a9d7ad09687a27e08c@68.183.32.158:26656,16738162b57072507fb436fd99d906909c126b2f@65.108.232.238:17656,ed12aee3273baaaf01e357574c1692f12776446d@65.109.117.165:50656,9ebe723eef929e9eff748f4046d6130ee349a398@65.108.203.149:24017,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,9aeb9250f279c9e288b7db702380e2970a36e248@5.188.118.105:46656,323d4309091003ea96ec3076b8bf4dc319c71345@109.205.182.137:26656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,8fbfa810cb666ddef1c9f4405e933ef49138f35a@65.108.199.120:54656,a9bcb95ee047c4a909c675dc36c556eafe1248e1@195.201.174.109:46656,bab2e24e088af1efc88684a83024fa31baad34e5@185.137.122.106:26656,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,62fa77951a7c8f323c0499fff716cd86932d8996@65.108.199.36:24214,7bf4e4a18bf2006f79f50c79903f77d4e2a5a303@65.21.77.175:33307,8036aed2d37890ddf245e7288b4fc724a301d728@65.109.117.23:50656,8b6c75d20ac3ceeb7f0f1d4b5fc89a69e567c47b@65.108.231.238:36656,4764a447ea3518e5017756b42ca5f6442b2f5768@5.161.114.1:26656,1e2a49792b0e0686827ec0fbc101a9ad709e0f28@88.210.9.78:26656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,5acc5ccc09dc10f5bc12c4ba4468a03c3df9d1ea@65.108.8.28:61356,863a266ca1a958b9d122511289041905120e26dd@185.245.183.254:26656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
