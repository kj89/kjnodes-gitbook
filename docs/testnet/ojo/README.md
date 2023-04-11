# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/ojo.png" width="150" alt=""><figcaption></figcaption></figure>

Ojo is a decentralized security-first oracle network built  to support the Cosmos Ecosystem. Ojo will source price data  from a diverse catalog of on and off-chain sources and use  advanced security mechanisms to guarantee the integrity of the data it provides.

**Chain ID**: ojo-devnet | **Latest Version Tag**: v0.1.2 | **Wasm**: OFF

[Website](https://ojo.network) | [Discord](https://discord.gg/fd8Yrex8nC) | [Twitter](https://twitter.com/ojo_network)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


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

**live-peers** (30)
```bash
peers="f3e3a1d7684f3af1d434596e9b70ab21f4d67838@165.232.119.140:26656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,9a60cf2bb51eed575d58170fcc55901fb99b40a0@194.163.148.202:50656,2905d22a658a7138c03c0259fba4c168260682bb@159.69.208.78:26656,4b54b62848bc09a68fc2cacb354fc6fcd10c8472@49.12.123.97:56656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,899892b43b951a5bb03cb2054e4d84f6431249cc@212.227.160.56:26656,99a183e0dcbbaf77125c3afdb1d7d48cc557d62b@161.97.134.64:50656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,bab2e24e088af1efc88684a83024fa31baad34e5@185.137.122.106:26656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,4e38368e64b1951439e7d6ac3387dae9dcfef120@94.130.16.254:60956,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,124439d1c16b1ee7ca1a39961f02fadf8539cb81@38.102.85.10:26656,3cd8b55fbb2c4e87ee5e39554155051d0d98edc4@188.34.187.252:50656,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,b0968b57bcb5e527230ef3cfa3f65d5f1e4647dd@35.212.224.95:26656,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,1c69ce0386cf66825a906a6b91bc55fcd5924f8b@194.233.89.251:50656,ed12aee3273baaaf01e357574c1692f12776446d@65.109.117.165:50656,67e95aeec46d7c5840f9685ca2b4cd725841b814@16.163.74.176:26636,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,4ffdad68a6c6302168e0951766ffa1921c9b19a4@199.175.98.136:26656,4bfc6d62d115a2440f9e5dc10c21d302dbdf5c64@34.220.136.165:26656,69774d64905bb33ea805228ac875835aea09f25a@185.217.198.141:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
