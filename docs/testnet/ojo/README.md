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

**live-peers** (29)
```bash
peers="1b81440d84a2746af6fba80c1a3a091f298f7a7a@185.206.214.254:26656,23830179727e6e38933e95000cb84ece4112f78c@185.155.97.74:18656,b16d876c443850cd358596790411b835d3f1735b@95.214.53.46:35656,66b140833cba7cadd92d544088d735e219adbf01@65.108.226.183:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,f3e3a1d7684f3af1d434596e9b70ab21f4d67838@165.232.119.140:26656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,58f192f7c6aebe881f54bd133e9b8abf82bc3b20@65.108.13.154:36656,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,dd55e293588003da8cd6cf56a0e6c6cdab1f6e75@65.109.88.254:46656,5acc5ccc09dc10f5bc12c4ba4468a03c3df9d1ea@65.108.8.28:61356,05147e2f262aec14447928ffb9a7687f207ef12c@178.208.252.54:29656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,622e5b7bc26be4edc4a9112ed0c5c8b00aa72721@185.246.84.196:26656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,0d4dc8d9e80df99fdf7fbb0e44fbe55e0f8dde28@65.108.205.47:14756,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,23da6727d574bd04ac40cc8c9cbe301ba8dbdc34@185.198.27.139:32656,9a60cf2bb51eed575d58170fcc55901fb99b40a0@194.163.148.202:50656,81d09ca7ba8f30812402f9076aad78e47f0afc7a@184.174.37.152:50656,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,bd90b71f1f982ebb18857da8cb777883d6ca687e@185.209.223.68:26656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,577606f2072f97a5107bead5b2321302092c1f7d@194.5.152.12:26656,2086389fe8bb43133205d1a76792b5e58bc9f811@65.108.197.164:64646"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
