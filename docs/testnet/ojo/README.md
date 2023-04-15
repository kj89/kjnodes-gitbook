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
peers="1b5c5927e6e3685b3e9fc278ca4c9d7002d4cc10@65.21.134.250:17656,c735f993287716ca1c358e9fe104dc570cf2ef3c@176.37.119.156:26694,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,a23cc4cbb09108bc9af380083108262454539aeb@35.215.116.65:26656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,06f673591d9302c2beab5130b77bbb0a6a69364d@116.202.227.117:50656,0ccc4bd8386fbec1421e3c19c24124eeb00b3293@46.101.144.90:28656,23da6727d574bd04ac40cc8c9cbe301ba8dbdc34@185.198.27.139:32656,bef511f2c5244e6603bd74295e2dffb126d04f41@158.101.208.86:26656,eddfe8bf3c478fdd0281808371f9d9d1a3d63308@157.90.208.222:60956,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,4cb932af43e2c64a0277516d96410a05294653de@75.119.148.69:26656,46be755bb7f34a6f4722713e40c9786266654396@38.242.237.125:26656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,371f313df7f79b34d65f026769a3e0c3e77127eb@45.137.67.238:26656,50ad0e558d9da6fce98ae4527cd49ee3e8d19940@94.250.202.215:26656,f3e3a1d7684f3af1d434596e9b70ab21f4d67838@165.232.119.140:26656,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,fee808fc235e2f345caaaee1d65f818d710f6433@213.137.237.201:26656,3c6384ae2a167912a5ace2f5f8e38afc559715f0@75.119.156.88:26656,3aeec94e9567c66ad6bb76b496aff6d55fd53d32@65.109.171.22:26656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,da369d44c00dba309237b21391806504353d188f@194.163.187.175:50656,dd100ed6f1046f8db6d1d7ad04ed6253f935e9b2@176.118.198.128:26656,b0dac6c4a34dff86d3a77665c61bd08b4a5007cf@65.108.224.156:26656,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,57847cb629cd707515b838a5baaf2b5c3ca0b022@65.108.199.206:37656,b6c75d1fbdc9c39daaaf52a4c0937b9f06975808@167.235.198.193:46656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
