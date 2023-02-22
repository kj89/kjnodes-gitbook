# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.1 | **Wasm**: OFF

[Website](https://islamiccoin.net) | [Discord](https://discord.gg/hU9MHG5kZq) | [Twitter](https://twitter.com/Islamic_Coin)




## Chain explorer
[https://explorer.kjnodes.com/haqq-testnet](https://explorer.kjnodes.com/haqq-testnet)

## Public endpoints

* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)
* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* grpc: [https://haqq-testnet.grpc.kjnodes.com](https://haqq-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@haqq-testnet.rpc.kjnodes.com:35656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@haqq-testnet.rpc.kjnodes.com:35659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/haqq-testnet/addrbook.json > $HOME/.haqqd/config/addrbook.json
```

**live-peers** (40)
```bash
peers="077d5d9169efb4b070ce7895d680a9d2148d522c@195.201.195.40:36656,7f2828e3910a4b165a65e5bfb2465c1e809bad3b@65.108.48.182:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,dd5ebfba86d8b5ff9c6ea3eb340fdb30e4c6990f@162.55.102.45:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,4990ed7074424046184dd474df40902c30f34182@65.108.250.241:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,bb3eecca04ac25ffa71175e77212eb2b88de6064@149.102.133.71:35656,2ad882b4126cc2ff75c24186ead4bfadb9bc6ae7@116.203.39.166:26656,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,62bf004201a90ce00df6f69390378c3d90f6dd7e@45.83.173.19:26656,3afcd044314bff8a2b3579b545e642edbd80396d@154.26.157.237:35656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,f1b1df46afd4c9d4f66051437078c0b85bc6b67b@65.108.206.118:61056,47a269c3e30f70d8234a2afd8e9055e74129fde0@65.108.129.29:36656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,eb503dddcc41ba801c646d63cc762de4e9c43aa4@35.228.23.164:26656,78e3ef8adf819b479acc13a2f92ab5c0fa350aeb@66.45.231.30:11464,6ce864d853904ebef9400528f129d8fefa6f1827@91.211.251.232:36656,9eb507f9365313dbe7f426050fec9648298f58ee@109.205.183.51:26656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,70c1b8334bf08fe5d56fb53d07da11f01faa560b@65.109.30.90:26656,46d146f78218ca4c00606254a1e059ef0c42e294@154.26.157.226:35656,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,23a1176c9911eac442d6d1bf15f92eeabb3981d5@45.83.173.18:26656,b1c07038b5b9b96d6fb35e4bb417af7ed238e733@95.217.35.186:26656,d43289f43e6fba3aaa51559d35b377907dd12007@65.108.234.11:11656,64a840f6f5344a22a485b2818f9da9a457d42827@95.217.57.232:36656,f50b6abb555c0d420834860d9a8f499801bb3ae8@135.181.62.222:26656,d8d8378108d4963ecdbb50e2f1712bc6f785f52c@154.26.157.227:35656,181c3ef9dba190c45ad8143550188d24e471b7a5@148.251.47.69:16656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,6e321bac32fbf035a7bf2085d02a40c88da0e7e0@149.102.133.68:35656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
