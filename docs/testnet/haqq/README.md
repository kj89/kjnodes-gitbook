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

**live-peers** (34)
```bash
peers="f909e50b6f27a964ae20d982d300f1137cb3bef2@144.76.90.130:30656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,1c5a4624a7f1a71e240ae2df82e97d5e9f46ff5c@88.99.214.188:60956,0833039f717227ccd156d156ea772746b8ac6d71@146.19.24.139:26656,23a1176c9911eac442d6d1bf15f92eeabb3981d5@45.83.173.18:26656,dd5ebfba86d8b5ff9c6ea3eb340fdb30e4c6990f@162.55.102.45:26656,62bf004201a90ce00df6f69390378c3d90f6dd7e@45.83.173.19:26656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,2ddd301131ac37ea58a390361cfaeb6701645ee5@117.62.66.67:35656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,1fefb6b75431482502e125a290deba1e7e539d4e@135.181.148.11:26656,ba56c564a5430632e59e2b08fc348735bc56b32f@154.12.232.140:26656,b72f2156db8c87e679dc853730746ff40038120c@213.239.215.77:26656,64a840f6f5344a22a485b2818f9da9a457d42827@95.217.57.232:36656,b9e8ec4eeb359e1b3cf5675563e72787b9d40adf@95.217.132.146:26656,eb503dddcc41ba801c646d63cc762de4e9c43aa4@35.228.23.164:26656,1b9b907b4bf609c7acf47a20bd23320c9e73b784@135.181.222.185:16656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,bc777df96c83c0433561c88c541dbbc520928f6c@195.3.221.239:26656,78e3ef8adf819b479acc13a2f92ab5c0fa350aeb@66.45.231.30:11464,ccff2d110a06e8a76fd1529200d96316eb077007@65.108.78.116:46656,d0accd9548e71c763394ab6a49d80ce4f124a9d5@3.127.31.113:26656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,022360b6d3bbae324b0cca90f80f6322576e2b42@23.88.70.109:12656,e2fde948646175b1b49b3e1943063b049e442917@154.26.157.238:35656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
