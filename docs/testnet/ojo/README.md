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

**live-peers** (40)
```bash
peers="8671c2dbbfd918374292e2c760704414d853f5b7@35.215.121.109:26656,06f673591d9302c2beab5130b77bbb0a6a69364d@116.202.227.117:50656,34a4c8433adfc4bf0df7c085ce58ed48664fbdc1@85.10.193.246:31656,3de750927e66b01bb566c1c189beeb43b7cde73f@213.239.216.252:47656,3c6384ae2a167912a5ace2f5f8e38afc559715f0@75.119.156.88:26656,315350f9d96426d4a025dbdecae84ceca64d1638@95.217.40.230:56656,f6d6e625759814e157457a5889961e02dba26ba6@65.109.92.240:37096,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,d5b2ae8815b09a30ab253957f7eca052dde3101d@65.108.9.164:24656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,1145755896d6a3e9df2f130cc2cbd223cdb206f0@209.145.53.163:29656,f4663c5df8ee2e2b6e1cc6a9d7ad09687a27e08c@68.183.32.158:26656,b6b4a4c720c4b4a191f0c5583cc298b545c330df@65.109.28.219:21656,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,978cf9aca38f819fd8189272379fc3c2ae2682a8@213.239.218.210:56656,67a1f07c7743d9bec92e11faad5bffe9bc08a178@130.185.119.243:50656,5a36595613f189a3c1096729897fb02be0a8c15e@89.117.50.187:28656,725988cccb088855f4fd5a1548aaa08b7bafec96@65.108.43.58:27675,8f414276a2cb7a97d37a3e126c186972e1968039@65.108.4.233:56656,8a8b9a8a58c922a7693715100710697ec69b1478@65.109.92.235:11086,3a2c9a7631c26006a5d1943c004ab2da8c04d7b7@5.161.201.79:26656,b16d876c443850cd358596790411b835d3f1735b@95.214.53.46:35656,fb45d68ce227d2bd3b112d26d27341faebc3736e@78.46.61.117:03656,3c8b9cf60b33bdd8b41db6d8af1009e91e14afc8@5.78.67.243:26656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,108037355c949c6fb4d7618f5ae04cbdc66c3362@65.108.206.96:27656,1b5c5927e6e3685b3e9fc278ca4c9d7002d4cc10@65.21.134.250:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,b0968b57bcb5e527230ef3cfa3f65d5f1e4647dd@35.212.224.95:26656,9f53e51449968bb2d2faad15dc4220757c4c33cd@213.239.215.77:47656,d9df87e2e26db62ef4014ce6e8705ee11bda304f@176.124.220.21:4669,dd55e293588003da8cd6cf56a0e6c6cdab1f6e75@176.37.119.156:26694,9bcec17faba1b8f6583d37103f20bd9b968ac857@38.146.3.230:21656,16738162b57072507fb436fd99d906909c126b2f@65.108.232.238:17656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,f6f9a074987ec9ed45f3a53cbd54e0f358a8648f@75.119.159.226:60656,e2e2ddece5e7f0aa4c3e47a6738a92aa1713ca73@67.217.57.70:26656,cb706ebe1d7a1f1d3e281bf46a78d84251f50810@95.216.14.72:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
