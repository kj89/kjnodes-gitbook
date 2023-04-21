# Services

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.1 | **Wasm**: OFF

[Website](https://islamiccoin.net) | [Discord](https://discord.gg/hU9MHG5kZq) | [Twitter](https://twitter.com/Islamic_Coin)



Subscribe to our free [🤖 Testnet Proposal Bot](https://t.me/kjnodes_testnet_proposal_bot) to never miss upcoming proposals


## Chain explorer
[https://explorer.kjnodes.com/haqq-testnet](https://explorer.kjnodes.com/haqq-testnet)

## Public endpoints

* api: [https://haqq-testnet.api.kjnodes.com](https://haqq-testnet.api.kjnodes.com)
* rpc: [https://haqq-testnet.rpc.kjnodes.com](https://haqq-testnet.rpc.kjnodes.com)
* grpc: haqq-testnet.grpc.kjnodes.com:35090

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

**live-peers** (30)
```bash
peers="62a8610cc2325cbdf25099b973ae488a05f7d417@65.108.206.57:13656,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,442d3bacb350437b8d9f0f1431e0519b81094100@135.181.62.222:26656,230d299006a432b0f44534ca8a19c8c876c0ccb3@85.10.193.246:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,29731457774b61da8186b9c764e8f7c1e2465e3e@142.93.36.176:26656,ee4db669ed2ff87cb2a47f848fa061517eb47737@161.97.151.46:26656,62bf004201a90ce00df6f69390378c3d90f6dd7e@45.83.173.19:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,7e11f631cf4bae9284d79f431a86c99779d7e832@51.79.77.103:19656,4034efbff7c82e1a2d3908fefd2512552dea63f5@65.109.38.208:26651,78e3ef8adf819b479acc13a2f92ab5c0fa350aeb@66.45.231.30:11464,16f40215d018c7d657fef0bb5ce2950251d525d2@148.251.51.144:36656,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,23a1176c9911eac442d6d1bf15f92eeabb3981d5@45.83.173.18:26656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,b9e8ec4eeb359e1b3cf5675563e72787b9d40adf@95.217.132.146:26656,6ce864d853904ebef9400528f129d8fefa6f1827@91.211.251.232:36656,97fbe24743895fe58ee7fb6a60a3c7826494f446@65.109.58.237:26656,999e8d7da8b1baaba37d2556d60b8bfa8c0c1b40@149.102.132.104:35656,d7ac44bf8f8d760c3df1a8695145021f35feb985@34.88.220.124:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,302466457301efc7b12f61561b85ab366ece5659@142.132.248.253:26656,eb503dddcc41ba801c646d63cc762de4e9c43aa4@35.228.23.164:26656,3ba8280c245f4d63a8f7913aea64a5071f0c76d7@65.109.18.166:54656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
