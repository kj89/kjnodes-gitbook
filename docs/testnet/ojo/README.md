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

**live-peers** (37)
```bash
peers="fe8c46222c3a013115797176623597aafc16e33a@173.212.203.238:46656,f70138a8bbca35814ed947184821f8a561651793@185.234.69.143:30656,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,8f414276a2cb7a97d37a3e126c186972e1968039@65.108.4.233:56656,8e69c82fd42041a5eff49bcb94ae65c037aa45a9@65.109.87.88:26156,b6b4a4c720c4b4a191f0c5583cc298b545c330df@65.109.28.219:21656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,67e95aeec46d7c5840f9685ca2b4cd725841b814@16.163.74.176:26636,d5b2ae8815b09a30ab253957f7eca052dde3101d@65.108.9.164:24656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,f4663c5df8ee2e2b6e1cc6a9d7ad09687a27e08c@68.183.32.158:26656,b0968b57bcb5e527230ef3cfa3f65d5f1e4647dd@35.212.224.95:26656,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,3de7e03a2c6c50e5c38309d47ecfbf14ddf5304e@65.109.115.237:50656,863a266ca1a958b9d122511289041905120e26dd@185.245.183.254:26656,408ee86160af26ee7204d220498e80638f7874f4@161.97.109.47:38656,1b5c5927e6e3685b3e9fc278ca4c9d7002d4cc10@65.21.134.250:26656,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,91eba8f362b6c41d324ff26f316ce0b50d22b955@213.136.84.176:10656,8b6c75d20ac3ceeb7f0f1d4b5fc89a69e567c47b@65.108.231.238:36656,bab2e24e088af1efc88684a83024fa31baad34e5@185.137.122.106:26656,98981d7eef057a01274473363addb7f0b17e06fa@84.21.171.25:26656,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,5acc5ccc09dc10f5bc12c4ba4468a03c3df9d1ea@65.108.8.28:61356,4764a447ea3518e5017756b42ca5f6442b2f5768@5.161.114.1:26656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,56461d1fbf920239c237ca6b71cd4147b8aabe6f@206.81.11.89:50656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,50e9bd8647571268df2313df6c46ba9960c9f40e@178.128.88.30:26656,d1c5c6bf4641d1800e931af6858275f08c20706d@23.88.5.169:18656,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,93003c656ea73cf54164274f271dc5ccd1d493be@178.124.214.192:32656,4bfc6d62d115a2440f9e5dc10c21d302dbdf5c64@34.220.136.165:26656,1e2a49792b0e0686827ec0fbc101a9ad709e0f28@88.210.9.78:26656,e711b6631c3e5bb2f6c389cbc5d422912b05316b@213.239.216.252:40256"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
