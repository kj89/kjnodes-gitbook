# Services

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/nolus.png" width="150" alt=""><figcaption></figcaption></figure>

Nolus aims to be the leading DeFi Lease platform. The protocol  intends to become a tool for empowering people, simple to use, and highly efficient.

**Chain ID**: nolus-rila | **Latest Version Tag**: v0.1.39 | **Wasm**: ON

[Website](https://www.nolus.io) | [Discord](https://discord.gg/nolus-protocol) | [Twitter](https://twitter.com/NolusProtocol)




## Chain explorer
[https://explorer.kjnodes.com/nolus-testnet](https://explorer.kjnodes.com/nolus-testnet)

## Public endpoints

* api: [https://nolus-testnet.api.kjnodes.com](https://nolus-testnet.api.kjnodes.com)
* rpc: [https://nolus-testnet.rpc.kjnodes.com](https://nolus-testnet.rpc.kjnodes.com)
* grpc: [https://nolus-testnet.grpc.kjnodes.com](https://nolus-testnet.grpc.kjnodes.com)

## Peering

**state-sync**

```text
d5519e378247dfb61dfe90652d1fe3e2b3005a5b@nolus-testnet.rpc.kjnodes.com:43656
```

**seed-node**

```text
3f472746f46493309650e5a033076689996c8881@nolus-testnet.rpc.kjnodes.com:43659
```

**addrbook**
```bash
curl -Ls https://snapshots.kjnodes.com/nolus-testnet/addrbook.json > $HOME/.nolus/config/addrbook.json
```

**live-peers** (42)
```bash
peers="d5519e378247dfb61dfe90652d1fe3e2b3005a5b@65.109.68.190:43656,387393e38531ac010f500d294505232a77c88766@45.33.32.8:26656,7a1fc4d1cc0ffec7db6a2a15496136e62561b162@161.97.146.108:26656,5c2a752c9b1952dbed075c56c600c3a79b58c395@195.3.220.135:27016,e0aac09f3de68abf583b0e3994228ee8bd19d1eb@168.119.124.130:45659,33f4b7f56b6708526f0638162f020394de0ce5e9@65.21.229.33:28656,a502800f1e99446243d17db93778f9c8eaa3eee0@84.46.241.37:26656,1278e67b0f6523c20e665109dd092ef20d6fd70e@45.67.230.23:26656,5b7092ce1624e8a23a5d90897c4c5231fb7b1238@185.245.183.172:16656,48283100d4cf8068dc16ef1b10aacf092303ec2f@65.109.85.170:47656,9d761ce1e1dc54ded3ab82ce0256c27631b5e82c@173.212.241.80:43656,805f69593aeb23e78ae19b4adca24d0ddd513e12@38.242.141.147:26656,fcb82df30d2056c3af024fb389e173d683fe8229@65.108.105.48:19756,681ecb99467dd00a586d9499a1002f2829f1a02d@65.109.85.208:29656,67be97f5ef69a4f149fbef7970ba888e5b2c2cff@65.108.231.124:16656,5289137e6134895c5b3b82a9847869f2a889cdc0@65.108.97.58:2776,a95975f3a58e20ba1c518f3cbb1c23ef7569e4d4@14.241.82.87:26656,d6f7b2380e994c6b8f6fcb05b4a326ae2d1f202a@37.123.114.30:26656,6d5921160c688c2e4e3b510fcfa48496e74cf2c6@80.92.204.247:37656,7c2ea36064077da73d0ad5b60d8ef215acbee50b@161.97.79.100:36656,da97597846a17fe5e8150a60dc8152e1225b877d@135.181.16.252:32656,2d500ae8bddfa548ee0fb0ed969709d78a4015af@144.168.47.230:26656,3a365d1f16a5068f9349715e9ab3a350d913ddd5@188.232.7.146:37656,77f535f833732fa794f7c4837060ae7ecd98f3a4@89.163.142.196:43656,98907b8c92c003aa2d003bb5d47e5ae6e34b0732@77.51.200.79:46656,81ff6924175ccca5d1f09cb5d999f0e64852ccea@188.163.121.216:26656,e4b7228ccadf3180e6e323aa4c0c97946ac054dc@65.109.112.20:11134,b18f05bafd90cde6391d41880fc2d2461034a5de@20.189.72.168:26656,ee44651212ebd37186ba97e6d7edefefc9ed54fe@185.190.142.207:26656,7131043c4c45ac797f7412c4a804527e208af6b2@142.132.231.118:46656,236a2626ad46bb671b200883b6105350310372ef@135.181.81.65:37656,85c5ef9ff695574abdf1ab38fb1196bc6482aec5@89.252.21.37:26656,12bacde692c9f13918e8bcf4c9538c60421602ea@84.46.241.67:26656,8ca0bffdf45aa4aaa4624c6d4c3e258a8c595591@65.108.43.58:27659,301dcb25951a0ebd6a36e09e612c85dc3aea3767@95.70.160.37:26656,5bf83be8dfe52fe2c204300f1e9b1449487ce5af@88.99.164.158:1176,e62dd608a302ba4f815a7cd3cf3d7facafa0e171@135.181.123.154:16656,28cdf59b342cb19fe488e99fab754ccc90c379e3@185.196.21.104:26656,60c57c5b7215c84260249768cf66ae550142af9f@141.98.169.25:26656,55acbb36f6e18ce9d5034c1e0f615bf13ee1ae27@195.2.80.63:43656,12b146cd82c7142e9d8aeb4f246499927ecb1c0f@217.13.223.167:36656,71ad2a400e31641413083e46d7522f9b00fa1083@194.163.176.222:26656"
sed -i -e "s|^persistent_peers *=.*|persistent_peers = \"$peers\"|" $HOME/.nolus/config/config.toml
```
