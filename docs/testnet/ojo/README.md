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
peers="2691bb6b296b951400d871c8d0bd94a3a1cdbd52@65.109.93.152:33656,4cb932af43e2c64a0277516d96410a05294653de@75.119.148.69:26656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,f3e3a1d7684f3af1d434596e9b70ab21f4d67838@165.232.119.140:26656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,da369d44c00dba309237b21391806504353d188f@194.163.187.175:50656,8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,ed12aee3273baaaf01e357574c1692f12776446d@65.109.117.165:50656,2f739fc450015f90acc7f7199e77780d07616257@65.109.90.171:36656,d6318facf0de085644dcf8ba57bcc1725b6ec515@89.58.59.75:36656,124439d1c16b1ee7ca1a39961f02fadf8539cb81@38.102.85.10:26656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,bd90b71f1f982ebb18857da8cb777883d6ca687e@185.209.223.68:26656,bab2e24e088af1efc88684a83024fa31baad34e5@185.137.122.106:26656,d2489830a5e91ec214edfc54756512e4f89f2609@65.109.92.79:12656,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,7bc388e144f4c00dbe98006ba320645c10c0a4d6@139.99.68.119:50656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,d1c5c6bf4641d1800e931af6858275f08c20706d@23.88.5.169:18656,cbe534c7d012e9eb4e71a5573aee8acc1adf4bc6@65.108.41.172:28056,09e190d2605573581fa67ec4b9b55c8995aa9abf@207.244.236.87:50656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,f63f353c1e8b47b6fe1cbbda91b5a91673c155b3@89.163.132.156:36656,577606f2072f97a5107bead5b2321302092c1f7d@194.5.152.12:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
