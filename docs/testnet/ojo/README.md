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
peers="23830179727e6e38933e95000cb84ece4112f78c@185.155.97.74:18656,f474a520009496972515f843cdb835fc7d663779@65.109.23.114:21656,25edf9d95199a89bb868d40a7bbeb0ca1f940a65@159.223.77.250:28656,5c2a752c9b1952dbed075c56c600c3a79b58c395@95.214.52.139:27226,7186f24ace7f4f2606f56f750c2684d387dc39ac@65.108.231.124:12656,f3e3a1d7684f3af1d434596e9b70ab21f4d67838@165.232.119.140:26656,eb329e1907bc9a519e863824e57cf5222cf45ec9@143.198.145.207:28656,aa020c9fdae827a4f912b77786d8080c62a34857@178.120.245.178:27556,8f414276a2cb7a97d37a3e126c186972e1968039@65.108.4.233:56656,11bb322f6396a1ca67717cf162385ed250503e28@154.12.253.123:36656,67e95aeec46d7c5840f9685ca2b4cd725841b814@16.163.74.176:26636,34a4c8433adfc4bf0df7c085ce58ed48664fbdc1@85.10.193.246:31656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:50656,3fd91ce7928545f56eb9fbd61ebc355ade39021a@15.235.143.226:50656,b133dde2713a216a017399920419fcb1e084cdb2@136.243.88.91:7330,7416a65de3cc548a537dbb8bdf93dbd83fe401d2@78.107.234.44:26656,d1c5c6bf4641d1800e931af6858275f08c20706d@23.88.5.169:18656,5acc5ccc09dc10f5bc12c4ba4468a03c3df9d1ea@65.108.8.28:61356,eddfe8bf3c478fdd0281808371f9d9d1a3d63308@157.90.208.222:60956,9ea0473b3684dbf1f2cf194f69f746566dab6760@78.46.99.50:22656,5461b1ff958615ab65b97a788774c557921e72ec@89.117.57.201:19656,5a53ebe6e029f8a26b1bc6dd8fe9a8efd57202f6@167.71.194.75:28656,f702b19a4dae5ad813dabe3f529bf31c160a74e0@5.189.176.202:26656,a654bbc2b27134da4eb1fcc08f07a2c9ea0deec7@51.79.77.103:12656,cf2de6fcee7dd1e7bbe3413e9c182481f49eede0@65.108.9.164:21656,4f3ae90ab38c9c327654084a4f1ac9a89b097fc3@51.81.208.203:26656,2c40b0aedc41b7c1b20c7c243dd5edd698428c41@138.201.85.176:26696,941268bb05f91e8bbba2741cc7d48e84b6a52d09@38.242.213.118:35656,1761db35a0402af7d6008705a49dad5c9059ae63@195.231.38.226:28656,d18abe07d27a732e913a782d31b691087a76078d@88.99.164.158:37096"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.ojo/config/config.toml
```
