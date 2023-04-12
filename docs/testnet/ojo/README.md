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
peers="8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,23da6727d574bd04ac40cc8c9cbe301ba8dbdc34@185.198.27.139:32656,6cbb393c7b4b061a3b63d8061e67ce8fcf53f8d6@95.214.55.109:2626,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,0ac9841750afe017b882768b0e29e72b8296d6b0@104.194.8.68:46656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,f3e3a1d7684f3af1d434596e9b70ab21f4d67838@165.232.119.140:26656,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,239caa37cb0f131b01be8151631b649dc700cd97@95.217.200.36:46656,311b3a8649a24e4a816284b92f2f3af30ac292d7@51.195.89.114:21156,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,06f673591d9302c2beab5130b77bbb0a6a69364d@116.202.227.117:50656,3c6384ae2a167912a5ace2f5f8e38afc559715f0@75.119.156.88:26656,340f0623e9338a5c93baf2d8a8825718a86d3e8b@195.3.223.196:26656,cbe534c7d012e9eb4e71a5573aee8acc1adf4bc6@65.108.41.172:28056,bab2e24e088af1efc88684a83024fa31baad34e5@185.137.122.106:26656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,f35a6ea4693d24d3727a8e866acab2a9faa2ddbc@91.223.3.144:26256,0621bb73d18724cae4eb411e6b96765f95a3345e@178.63.8.245:61356,5af3d50dcc231884f3d3da3e3caecb0deef1dc5b@142.132.134.112:25356,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,69774d64905bb33ea805228ac875835aea09f25a@185.217.198.141:26656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,371f313df7f79b34d65f026769a3e0c3e77127eb@45.137.67.238:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
