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

**live-peers** (25)
```bash
peers="6fad54232f11a0306bd0d942c2ec5f9ba0ae2f1a@34.91.54.209:26656,51e4544568cf880451bfffc292de88adc472f0e0@34.147.126.38:26656,3df5a68b919177179c6dcb0b9c9354fd6bbba1c8@65.109.92.240:20116,d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:35656,23ff658b56fbb8bc73372973a34733ff5d79b435@142.132.202.50:11604,56158e0f2acf850114e82644afceb565a73b08cc@185.144.99.95:26656,6771e65c1b30cc514faf5943320fdda480fe9124@95.216.39.183:26656,ed145a35b436878c1f1c10634bd18600f3696e17@95.217.181.142:26656,360d7095f3c1250a013cfe66c43a3f0790782f78@84.46.254.50:26656,ccff2d110a06e8a76fd1529200d96316eb077007@65.108.78.116:46656,ce080696d69228597caf0e80920dfe1bae2dcd54@95.217.12.131:26656,59af99085c961a6a5c8dc4bc8b3abffda16ddccb@135.181.38.62:26656,9444cf6e8cc3e452f8006acce0283d87ee663b7a@185.163.125.253:35656,90b40d2b773090b82aa7788c2d1937e4fd6d2dc0@65.108.231.124:19656,d59dc597f0d41bcbc7ff53374686affb143726c2@51.195.203.103:35656,24e894d4d8a18276acf6051cccf369a1ce69842d@65.108.151.105:26656,64a840f6f5344a22a485b2818f9da9a457d42827@95.217.57.232:36656,2d13d679b64e1a574904a140f72815644ec71131@65.21.133.125:30656,00b1befaceba6b0178d2b6076ae0968adf4bd7b5@65.108.67.152:26656,ee4db669ed2ff87cb2a47f848fa061517eb47737@161.97.151.46:26656,efc12714ae801dcb228e79cf3980b8b8f4b86a88@148.251.53.202:36656,32a8eec046b95e8646ff0810b4596dc7083a0beb@65.108.145.131:26656,a884387139109784cad9193652b82ef20a85d713@38.242.159.148:26656,927a323649e7dd8d4c75da6e5edaee439652b46f@65.109.92.241:20116,5b2ee53c742ce5d392b93c8f193f489a4f13f685@5.189.186.222:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.haqqd/config/config.toml
```
