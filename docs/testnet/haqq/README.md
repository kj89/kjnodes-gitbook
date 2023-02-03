# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/haqq.png" width="150" alt=""><figcaption></figcaption></figure>

Haqq is the blockchain network that issues Islamic Coin,  its native cryptocurrency. Haqq is fast, trusted and  compatible with thousands of applications around the world.

**Chain ID**: haqq_54211-3 | **Latest Version Tag**: v1.3.0 | **Wasm**: OFF

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

**live-peers** (35)
```bash
peers="fd53be6145264c86f2db22659141c925e119794c@138.201.155.226:12656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,ccff2d110a06e8a76fd1529200d96316eb077007@65.108.78.116:46656,1e09d40584a277c72d6023e2956ff923c9d5e062@85.10.203.117:36656,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,077d5d9169efb4b070ce7895d680a9d2148d522c@195.201.195.40:36656,b72f2156db8c87e679dc853730746ff40038120c@213.239.215.77:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,16f40215d018c7d657fef0bb5ce2950251d525d2@148.251.51.144:36656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,6570de868d0f7a5b4dc9f5a007ba98319a7fa8b4@194.163.162.31:26656,00b1befaceba6b0178d2b6076ae0968adf4bd7b5@65.108.67.152:26656,8558de1d3062319bb877316c5c33e704f1e0a972@84.46.242.147:26656,dddce0afadf33e8b8c33a9e797493cd18a9ce5c7@154.26.157.240:35656,bb6c75744906248c25c65291b0f48637f11357fe@109.123.252.231:35656,f54d4de6d4ae81ec8a2315b54247872b315f198d@65.109.57.9:26656,64a840f6f5344a22a485b2818f9da9a457d42827@95.217.57.232:36656,7d730d99e7981f284d45c7af61cdbe2fcbae4bce@34.125.204.188:35656,78e3ef8adf819b479acc13a2f92ab5c0fa350aeb@66.45.231.30:11464,d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656,48a2a7762a579d25bca95b0a3548b714238dd60b@213.239.216.252:20656,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,331ca63236ba05842d561e22c0bcc8582efa60a1@209.126.80.192:26656,7094f2c1ee04801b76159bd614eb5947ffc8c5d9@109.71.177.3:35656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,f57fae1bdea281392b563a58978a2d8c0a37725f@95.217.233.234:26656,6ce864d853904ebef9400528f129d8fefa6f1827@91.211.251.232:36656,9444cf6e8cc3e452f8006acce0283d87ee663b7a@185.163.125.253:35656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
