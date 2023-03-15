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

**live-peers** (38)
```bash
peers="06f673591d9302c2beab5130b77bbb0a6a69364d@116.202.227.117:50656,622e5b7bc26be4edc4a9112ed0c5c8b00aa72721@185.246.84.196:26656,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,4609153f2b095b6c7f98b9cd3d079fe8fcd992db@95.216.14.58:61356,8f414276a2cb7a97d37a3e126c186972e1968039@65.108.4.233:56656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,cd4d7ffdad8bd258cd90c22ec7197c0fdf9f3648@38.242.134.73:27656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,d5b2ae8815b09a30ab253957f7eca052dde3101d@65.108.9.164:24656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,9015c79a2ae5a0033f4ee9237a19ea67579e37f8@135.181.57.104:26656,f4663c5df8ee2e2b6e1cc6a9d7ad09687a27e08c@68.183.32.158:26656,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,7bf4e4a18bf2006f79f50c79903f77d4e2a5a303@65.21.77.175:33307,50e9bd8647571268df2313df6c46ba9960c9f40e@178.128.88.30:26656,969b1e53d217abf769054777190f9a65eb8174cf@46.4.61.91:26656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,8b6c75d20ac3ceeb7f0f1d4b5fc89a69e567c47b@65.108.231.238:36656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,4764a447ea3518e5017756b42ca5f6442b2f5768@5.161.114.1:26656,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,b6a132b99a63edffeb761560c3e395bf3298de7f@155.138.145.250:26656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,f70138a8bbca35814ed947184821f8a561651793@185.234.69.143:30656,e7689e281278e2e52c95962cab219e681b641c1a@46.0.203.78:21656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,a3a9014f82cb69fe0494ea3bc49990027d081a5a@65.108.126.35:36656,4bfc6d62d115a2440f9e5dc10c21d302dbdf5c64@34.220.136.165:26656,57847cb629cd707515b838a5baaf2b5c3ca0b022@65.108.199.206:37656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,b0968b57bcb5e527230ef3cfa3f65d5f1e4647dd@35.212.224.95:26656,bab2e24e088af1efc88684a83024fa31baad34e5@185.137.122.106:26656,1e2a49792b0e0686827ec0fbc101a9ad709e0f28@88.210.9.78:26656,ae2b3551615ae4a7d0d4397b1a5f2d97509b468a@94.130.219.37:12656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
